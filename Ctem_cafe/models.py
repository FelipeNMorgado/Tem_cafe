from django.db import models

class Cadastro(models.Model):
    email = models.EmailField()
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
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    concordo_termos = models.BooleanField()

    def __str__(self):
        return self.email


    def __str__(self):
        return self.email
    


