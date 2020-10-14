import json

import psycopg2
import requests

from .serializers import ClientesSerializers, CadastradoSerializers, NaoCadastradoSerializers, InstaladoSerializers


def consulta_banco(email):
    try:
        conexao_db = psycopg2.connect(user="cliente_r",
                                      password="Cl13nt_R",
                                      host="168.196.104.12",
                                      port="5432",
                                      database="mkData3.0")

        cursor = conexao_db.cursor()

        query1 = '''
        SELECT row_to_json(row) FROM
        (SELECT codpessoa, nome_razaosocial, email FROM public.mk_pessoas WHERE email = %s LIMIT 1)row;
        '''

        query2 = '''
        SELECT row_to_json(row) FROM
        (SELECT p.codpessoa, p.nome_razaosocial, p.email, c.codconexao, pl.descricao FROM public.mk_pessoas as p
        INNER JOIN public.mk_conexoes as c ON c.codcliente = p.codpessoa
        INNER JOIN public.mk_planos_acesso as pl ON c.codplano_acesso = pl.codplano
        WHERE p.email = %s LIMIT 1) row;
        '''

        cursor.execute(query1, (email,))
        retorno_query1 = cursor.fetchone()
        if retorno_query1 is None:
            retorno_query2 = None
            return retorno_query1, retorno_query2
        elif retorno_query1 is not None:
            cursor.execute(query2, (email,))
            retorno_query2 = cursor.fetchone()
            return retorno_query1, retorno_query2

    except(Exception, psycopg2.Error) as error:
        print("Erro durante conexão com o banco:", error)

    finally:
        if conexao_db:
            cursor.close()
            conexao_db.close()
            print("Conexão com o banco encerrada")


def tratamento_dados(retorno_query1, retorno_query2):
    if retorno_query1 is None:
        cod_pessoa = None
        cod_conexao = None
        plano_acesso = None
        return cod_pessoa, cod_conexao, plano_acesso
    elif retorno_query2 is None:
        cod_pessoa = retorno_query1[0]['codpessoa']
        cod_conexao = None
        plano_acesso = None
        return cod_pessoa, cod_conexao, plano_acesso
    else:
        cod_pessoa = retorno_query2[0]['codpessoa']
        cod_conexao = retorno_query2[0]['codconexao']
        plano_acesso = retorno_query2[0]['descricao']
        return cod_pessoa, cod_conexao, plano_acesso


def serializar_cliente(dados_lead):
    serializer = ClientesSerializers(data=dados_lead)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer


def serializar_instalado(dados_lead):
    serializer = InstaladoSerializers(data=dados_lead)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer


def serializar_cadastrado(dados_lead):
    serializer = CadastradoSerializers(data=dados_lead)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer


def serializar_nao_cadastrado(dados_lead):
    serializer = NaoCadastradoSerializers(data=dados_lead)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer
