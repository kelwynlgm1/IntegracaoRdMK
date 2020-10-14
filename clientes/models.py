from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Clientes(Base):
    id = models.AutoField('ID: ', auto_created=True, primary_key=True, serialize=False)
    nome = models.CharField('Nome do cliente: ', max_length=100)
    email = models.EmailField('Email:', unique=True)
    cidade = models.CharField('Cidade: ', max_length=30, blank=True)
    telefone = models.CharField('Telefone: ', max_length=30, blank=True)

    class Meta:
        verbose_name = 'Cliente'

    def __str__(self):
        return self.nome


class Cadastrado(Base):
    id = models.AutoField('ID: ', auto_created=True, primary_key=True, serialize=False)
    nome = models.CharField('Nome do cliente: ', max_length=100)
    email = models.EmailField('Email:', unique=True)
    cidade = models.CharField('Cidade: ', max_length=30, blank=True)
    telefone = models.CharField('Telefone: ', max_length=30, blank=True)
    cod_pessoa = models.PositiveIntegerField('Código do cadastro ', null=False)

    class Meta:
        verbose_name = 'Clientes cadastrado'

    def __str__(self):
        return self.nome


class NaoCadastrado(Base):
    id = models.AutoField('ID: ', auto_created=True, primary_key=True, serialize=False)
    nome = models.CharField('Nome do cliente: ', max_length=100)
    email = models.EmailField('Email:', unique=True)
    cidade = models.CharField('Cidade: ', max_length=30, blank=True)
    telefone = models.CharField('Telefone: ', max_length=30, blank=True)
    registrado = models.BooleanField('Cadastro no MK', default=False)

    class Meta:
        verbose_name = 'Clientes não cadastrado'

    def __str__(self):
        return self.nome


class Instalado(Base):
    id = models.AutoField('ID: ', auto_created=True, primary_key=True, serialize=False)
    nome = models.CharField('Nome do cliente: ', max_length=100)
    email = models.EmailField('Email:', unique=True)
    cidade = models.CharField('Cidade: ', max_length=30, blank=True)
    telefone = models.CharField('Telefone: ', max_length=30, blank=True)
    cod_pessoa = models.PositiveIntegerField('Código do Cadastro: ', null=False)
    cod_conexao = models.PositiveIntegerField('Código da Conexão: ', null=False)
    plano_acesso = models.CharField('Plano contratado: ', null=False, max_length=100)

    class Meta:
        verbose_name = 'Clientes instalado'

    def __str__(self):
        return self.nome
