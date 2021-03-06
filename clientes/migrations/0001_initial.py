# Generated by Django 2.2.9 on 2020-10-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID: ')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do cliente: ')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email:')),
                ('cidade', models.CharField(blank=True, max_length=30, verbose_name='Cidade: ')),
                ('telefone', models.CharField(blank=True, max_length=30, verbose_name='Telefone: ')),
                ('cod_pessoa', models.PositiveIntegerField(verbose_name='Código do cadastro ')),
            ],
            options={
                'verbose_name': 'Clientes cadastrado',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID: ')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do cliente: ')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email:')),
                ('cidade', models.CharField(blank=True, max_length=30, verbose_name='Cidade: ')),
                ('telefone', models.CharField(blank=True, max_length=30, verbose_name='Telefone: ')),
            ],
            options={
                'verbose_name': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Instalado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID: ')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do cliente: ')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email:')),
                ('cidade', models.CharField(blank=True, max_length=30, verbose_name='Cidade: ')),
                ('telefone', models.CharField(blank=True, max_length=30, verbose_name='Telefone: ')),
                ('cod_pessoa', models.PositiveIntegerField(verbose_name='Código do Cadastro: ')),
                ('cod_conexao', models.PositiveIntegerField(verbose_name='Código da Conexão: ')),
                ('plano_acesso', models.CharField(max_length=100, verbose_name='Plano contratado: ')),
            ],
            options={
                'verbose_name': 'Clientes instalado',
            },
        ),
        migrations.CreateModel(
            name='NaoCadastrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID: ')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('atualizacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do cliente: ')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email:')),
                ('cidade', models.CharField(blank=True, max_length=30, verbose_name='Cidade: ')),
                ('telefone', models.CharField(blank=True, max_length=30, verbose_name='Telefone: ')),
                ('registrado', models.BooleanField(default=False, verbose_name='Cadastro no MK')),
            ],
            options={
                'verbose_name': 'Clientes não cadastrado',
            },
        ),
    ]
