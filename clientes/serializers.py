from rest_framework import serializers

from .models import Clientes, Instalado, NaoCadastrado, Cadastrado


class CadastradoSerializers(serializers.ModelSerializer):
    class Meta:
        '''extra_kwargs = {
        'email': {'write_only': True}
        }'''

        model = Cadastrado
        fields = (
            'id',
            'nome',
            'email',
            'cidade',
            'telefone',
            # 'cod_conexao',
            'cod_pessoa',
            # 'plano_acesso',
            # 'criacao',
            # 'atualizacao',
            # 'ativo',
            )


class NaoCadastradoSerializers(serializers.ModelSerializer):
    class Meta:
        '''extra_kwargs = {
        'email': {'write_only': True}
        }'''

        model = NaoCadastrado
        fields = (
            'id',
            'nome',
            'email',
            'cidade',
            'telefone',
            # 'cod_conexao',
            # 'cod_pessoa',
            # 'plano_acesso',
            # 'criacao',
            # 'atualizacao',
            # 'ativo',
            )


class InstaladoSerializers(serializers.ModelSerializer):
    class Meta:
        '''extra_kwargs = {
        'email': {'write_only': True}
        }'''

        model = Instalado
        fields = (
            'id',
            'nome',
            'email',
            'cidade',
            'telefone',
            'cod_conexao',
            'cod_pessoa',
            'plano_acesso',
            # 'criacao',
            # 'atualizacao',
            # 'ativo',
            )


class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        '''extra_kwargs = {
            'email': {'write_only': True}
        }'''

        model = Clientes
        fields = (
            'id',
            'nome',
            'email',
            'cidade',
            'telefone',
            #'cadastrado',
            #'instalado',
            #'nao_cadastrado',
            #'cod_conexao',
            # 'criacao',
            # 'atualizacao',
            # 'ativo',
        )
