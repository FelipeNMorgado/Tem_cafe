from django.db import models
from django.contrib.auth.models import User

class Cadastro(models.Model):
    email = models.EmailField(primary_key=True)
    senha = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    concordo_termos = models.BooleanField()



class Cliente(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    nome_completo = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    concordo_termos = models.BooleanField()

    def __str__(self):
        return self.email


    def __str__(self):
        return self.email
    

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=10)

    def str(self):
        return f'{self.user_id}'


class Avaliacao3(models.Model):
    avaliador = models.CharField(max_length=150)  # Campo para armazenar o nome do usuário que fez a avaliação
    avaliado = models.CharField(max_length=100)
    nota = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)