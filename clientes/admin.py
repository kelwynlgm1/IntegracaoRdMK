from django.contrib import admin
from .models import Clientes, Cadastrado, Instalado, NaoCadastrado


@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade', 'telefone', 'criacao')


@admin.register(Cadastrado)
class CadastradoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade', 'telefone', 'criacao', 'cod_pessoa')


@admin.register(Instalado)
class InstaladoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade', 'telefone', 'criacao', 'cod_pessoa', 'cod_conexao', 'plano_acesso')


@admin.register(NaoCadastrado)
class NaoCadastradoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cidade', 'telefone', 'criacao', 'registrado')
