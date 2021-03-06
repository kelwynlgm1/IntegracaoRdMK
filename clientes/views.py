import json

import requests
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Clientes, Cadastrado, NaoCadastrado, Instalado
from .serializers import ClientesSerializers, InstaladoSerializers, CadastradoSerializers, NaoCadastradoSerializers
from .funcoes import consulta_banco, tratamento_dados, serializar_instalado, serializar_nao_cadastrado, \
    serializar_cadastrado, serializar_cliente


def index(request):
    return render(request, 'index.html')


def get_response(request):
    return HttpResponse("OK")


class PostAPIView(APIView):
    """
    API DE LEADS RD STATION
    """

    def post(self, request):
        retorno = request.data['leads'][0]['last_conversion']['content']
        telefone = request.data['leads'][0]['mobile_phone']
        if telefone is None:
            telefone = request.data['leads'][0]['personal_phone']
        print("***", telefone)
        if retorno['Você já é nosso cliente?'] == "Ainda não sou cliente":
            retorno_query1, retorno_query2 = consulta_banco(retorno['email_lead'])
            cod_pessoa, cod_conexao, plano_acesso = tratamento_dados(retorno_query1, retorno_query2)
            cidade_cliente = retorno.get('Sua cidade')
            if cidade_cliente is not None and cod_pessoa is None and cod_conexao is None:
                dados_lead = {
                    "nome": retorno['Nome'],
                    "email": retorno['email_lead'],
                    "cidade": retorno['Sua cidade'],
                    "telefone": telefone,
                }
                serializer = serializar_nao_cadastrado(dados_lead)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            if cidade_cliente is not None and cod_pessoa is not None and cod_conexao is None:
                dados_lead = {
                    "nome": retorno['Nome'],
                    "email": retorno['email_lead'],
                    "cidade": retorno['Sua cidade'],
                    "telefone": telefone,
                    "cod_pessoa": cod_pessoa
                }
                serializer = serializar_cadastrado(dados_lead)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            if cidade_cliente is not None and cod_pessoa is not None and cod_conexao is not None:
                dados_lead = {
                    "nome": retorno['Nome'],
                    "email": retorno['email_lead'],
                    "cidade": retorno['Sua cidade'],
                    "telefone": telefone,
                    "cod_conexao": cod_conexao,
                    "cod_pessoa": cod_pessoa,
                    "plano_acesso": plano_acesso
                }
                serializer = serializar_instalado(dados_lead)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            if cidade_cliente is None and cod_pessoa is None and cod_conexao is None:
                dados_lead = {
                    "nome": retorno['Nome'],
                    "email": retorno['email_lead'],
                    "cidade": "Cidade não informada",
                    "telefone": telefone,
                }
                serializer = serializar_nao_cadastrado(dados_lead)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            if cidade_cliente is None and cod_pessoa is not None and cod_conexao is None:
                dados_lead = {
                    "nome": retorno['Nome'],
                    "email": retorno['email_lead'],
                    "cidade": "Cidade não informada",
                    "telefone": telefone,
                    "cod_pessoa": cod_pessoa
                }
                serializer = serializar_cadastrado(dados_lead)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            if cidade_cliente is None and cod_pessoa is not None and cod_conexao is not None:
                dados_lead = {
                    "nome": retorno['Nome'],
                    "email": retorno['email_lead'],
                    "cidade": "Cidade não informada",
                    "telefone": telefone,
                    "cod_conexao": cod_conexao,
                    "cod_pessoa": cod_pessoa,
                    "plano_acesso": plano_acesso
                }
                serializer = serializar_instalado(dados_lead)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse("Já é cliente. Lead não contabilizada", status=status.HTTP_200_OK)


class UpdateApiView(APIView):
    """
    API DE LEADS RD STATION
    """
    def post(self, request):
        retorno = request.data
        print(retorno)
        retorno_query1, retorno_query2 = consulta_banco(retorno['email'])
        cod_pessoa, cod_conexao, plano_acesso = tratamento_dados(retorno_query1, retorno_query2)
        cidade_cliente = retorno.get('cidade')
        print(cod_pessoa, cod_conexao, plano_acesso)
        if cidade_cliente is not None and cod_pessoa is None and cod_conexao is None:
            dados_lead = {
                "nome": retorno['nome'],
                "email": retorno['email'],
                "cidade": retorno['cidade'],
                "telefone": retorno['telefone']
            }
            serializer = serializar_nao_cadastrado(dados_lead)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if cidade_cliente is not None and cod_pessoa is not None and cod_conexao is None:
            dados_lead = {
                "nome": retorno['nome'],
                "email": retorno['email'],
                "cidade": retorno['cidade'],
                "telefone": retorno['telefone'],
                "cod_pessoa": cod_pessoa
            }
            serializer = serializar_cadastrado(dados_lead)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if cidade_cliente is not None and cod_pessoa is not None and cod_conexao is not None:
            dados_lead = {
                "nome": retorno['nome'],
                "email": retorno['email'],
                "cidade": retorno['cidade'],
                "telefone": retorno['telefone'],
                "cod_conexao": cod_conexao,
                "cod_pessoa": cod_pessoa,
                "plano_acesso": plano_acesso
            }
            serializer = serializar_instalado(dados_lead)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if cidade_cliente is None and cod_pessoa is None and cod_conexao is None:
            dados_lead = {
                "nome": retorno['nome'],
                "email": retorno['email'],
                "cidade": "Cidade não informada",
                "telefone": retorno['telefone']
            }
            serializer = serializar_nao_cadastrado(dados_lead)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if cidade_cliente is None and cod_pessoa is not None and cod_conexao is None:
            dados_lead = {
                "nome": retorno['nome'],
                "email": retorno['email'],
                "cidade": "Cidade não informada",
                "telefone": retorno['telefone'],
                "cod_pessoa": cod_pessoa
            }
            serializer = serializar_cadastrado(dados_lead)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if cidade_cliente is None and cod_pessoa is not None and cod_conexao is not None:
            dados_lead = {
                "nome": retorno['nome'],
                "email": retorno['email'],
                "cidade": "Cidade não informada",
                "telefone": retorno['telefone'],
                "cod_conexao": cod_conexao,
                "cod_pessoa": cod_pessoa,
                "plano_acesso": plano_acesso
            }
            serializer = serializar_instalado(dados_lead)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CadastradoApiView(APIView):
    def get(self, request):
        cadastrados = Cadastrado.objects.all()
        serializer = CadastradoSerializers(cadastrados, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        cliente = Cadastrado.objects.get(pk=id)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NaoCadastradoApiView(APIView):
    def get(self, request):
        nao_cadastrados = NaoCadastrado.objects.all()
        serializer = NaoCadastradoSerializers(nao_cadastrados, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        nao_cadastrado = NaoCadastrado.objects.get(pk=id)
        nao_cadastrado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InstaladoApiView(APIView):
    def get(self, request):
        instalados = Instalado.objects.all()
        serializer = InstaladoSerializers(instalados, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        nao_cadastrado = NaoCadastrado.objects.get(pk=id)
        nao_cadastrado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientesApiView(APIView):
    def get(self, request):
        clientes = Clientes.objects.all()
        serializer = ClientesSerializers(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        retorno = request.data['leads'][0]['last_conversion']['content']
        telefone = request.data['leads'][0]['mobile_phone']
        if telefone is None:
            telefone = request.data['leads'][0]['personal_phone']
        print("***", telefone)
        if retorno.get('Sua cidade') is not None:
            dados_lead2 = {
                "nome": retorno['Nome'],
                "email": retorno['email_lead'],
                "cidade": retorno['Sua cidade'],
                "telefone": telefone
            }
        elif retorno.get('Sua cidade') is None:
            dados_lead2 = {
                "nome": retorno['Nome'],
                "email": retorno['email_lead'],
                "cidade": "Cidade não informada",
                "telefone": telefone
            }
        serializer = serializar_cliente(dados_lead2)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        cliente = NaoCadastrado.objects.get(pk=id)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def update_cliente(request):
    if request.method == "POST":
        link = requests.get('https://novaapirdmk-kl.herokuapp.com/api/v1/visualiza/nao_cadastrados')
        retorno = json.loads(link.text)
        for retorno in retorno:
            print("***", retorno)
            query1, query2 = consulta_banco(retorno['email'])
            cod_pessoa, cod_conexao, plano_acesso = tratamento_dados(query1, query2)
            if cod_pessoa is not None:
                link_delete = 'https://novaapirdmk-kl.herokuapp.com/api/v1/deleta/nao_cadastrados/' + str(retorno['id']) + '/'
                deleta = requests.delete(url=link_delete)
                assert deleta.status_code == 204
                dados_lead = {
                    "nome": retorno['nome'],
                    "email": retorno['email'],
                    "cidade": retorno['cidade'],
                    "telefone": retorno['telefone']
                }
                link_post = "https://novaapirdmk-kl.herokuapp.com/api/v1/update/clientes"
                envio = requests.post(url=link_post, data=dados_lead)
                assert envio.status_code == 201
        return render(request, 'atualizado.html')
    else:
        return render(request, 'atualizado.html')


def update_cliente_cadastrado(request):
    if request.method == "POST":
        link = requests.get('https://novaapirdmk-kl.herokuapp.com/api/v1/visualiza/cadastrados')
        retorno = json.loads(link.text)
        for retorno in retorno:
            print("***", retorno)
            query1, query2 = consulta_banco(retorno['email'])
            cod_pessoa, cod_conexao, plano_acesso = tratamento_dados(query1, query2)
            if cod_conexao is not None:
                link_delete = 'https://novaapirdmk-kl.herokuapp.com/api/v1/deleta/cadastrados/' + str(retorno['id']) + '/'
                deleta = requests.delete(url=link_delete)
                assert deleta.status_code == 204
                dados_lead = {
                    "nome": retorno['nome'],
                    "email": retorno['email'],
                    "cidade": retorno['cidade'],
                    "telefone": retorno['telefone']
                }
                link_post = "https://novaapirdmk-kl.herokuapp.com/api/v1/update/clientes"
                envio = requests.post(url=link_post, data=dados_lead)
                assert envio.status_code == 201
        return render(request, 'atualizado.html')
    else:
        return render(request, 'atualizado.html')
