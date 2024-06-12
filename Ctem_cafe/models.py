from django.db import models
from django.contrib.auth.models import User

class Cadastro2(models.Model):
    email = models.EmailField(primary_key=True)
    senha = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    descricao = models.TextField()
    arq = models.URLField()
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
    

class Avaliacao3(models.Model):
    avaliador = models.CharField(max_length=150)  # Campo para armazenar o nome do usuário que fez a avaliação
    avaliado = models.CharField(max_length=100)
    nota = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class TagCafeteria3(models.Model):
    cafeteria = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_id.username} - {self.tag_name}'
    

class Favorite3(models.Model):
    usuario = models.CharField(max_length=150)  # Campo para armazenar o nome do usuário que fez a avaliação
    cafeteria = models.CharField(max_length=100)
    value = models.CharField(choices=[('like', 'Like'), ('unlike', 'Unlike')], max_length=10)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class TagUsuario(models.Model):
    usuario = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_id.username} - {self.tag_name}'
    

class Noticias(models.Model):
    cafeteria = models.CharField(max_length=100)
    arq = models.URLField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
