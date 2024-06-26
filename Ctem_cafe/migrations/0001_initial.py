# Generated by Django 5.0.4 on 2024-04-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=100)),
                ('nome_loja', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('concordo_termos', models.BooleanField()),
            ],
        ),
    ]
