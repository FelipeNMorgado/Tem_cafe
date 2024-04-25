
from django.shortcuts import render, redirect
from .models import Cadastro
from .models import Cliente
from .models import Favorite

def home(request):
    return render(request, 'index.html')  # Supondo que você tenha um template chamado index.html

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastroloja.html')
    elif request.method == "POST":
        email = request.POST.get('inputEmail4')
        senha = request.POST.get('inputPassword4')
        nome_loja = request.POST.get('inputStoreName')
        endereco = request.POST.get('inputAddress')
        complemento = request.POST.get('inputAddress2')
        cidade = request.POST.get('inputCity')
        bairro = request.POST.get('inputNeighborhood')
        estado = request.POST.get('inputState')
        cep = request.POST.get('inputZip')
        concordo_termos = request.POST.get('gridCheck')

        # Crie uma instância do modelo Cadastro com os dados do formulário
        cadastro = Cadastro(
            email=email,
            senha=senha,
            nome_loja=nome_loja,
            endereco=endereco,
            complemento=complemento,
            cidade=cidade,
            bairro=bairro,
            estado=estado,
            cep=cep,
            concordo_termos=concordo_termos
        )
        # Salve os dados no banco de dados
        cadastro.save()

        return redirect('home')  # Atualize isso com a URL desejada após o cadastro
    
def cadastro_cliente(request):
    if request.method == "GET":
        return render(request, 'cadastro_cliente.html')
    elif request.method == "POST":
        email = request.POST.get('inputEmail4')
        senha = request.POST.get('inputPassword4')
        nome_completo = request.POST.get('inputFullName')
        endereco = request.POST.get('inputAddress')
        complemento = request.POST.get('inputAddress2')
        cidade = request.POST.get('inputCity')
        bairro = request.POST.get('inputNeighborhood')
        estado = request.POST.get('inputState')
        cep = request.POST.get('inputZip')
        telefone = request.POST.get('inputPhone')
        data_nascimento = request.POST.get('inputBirthDate')
        concordo_termos = request.POST.get('gridCheck')

        cliente = Cliente(
            email=email,
            senha=senha,
            nome_completo=nome_completo,
            endereco=endereco,
            complemento=complemento,
            cidade=cidade,
            bairro=bairro,
            estado=estado,
            cep=cep,
            telefone=telefone,
            data_nascimento=data_nascimento,
            concordo_termos=concordo_termos
        )
        cliente.save()

        return redirect('home')

    
def perfil(request):
    return render(request, 'visperfil.html')



def menu(request):

    user = request.user
    
    # Busca todas as instâncias de favoritos do usuário
    favorites = Favorite.objects.filter(user_id=user.id)

    is_favorited = favorites.filter(user_id = user.id).exists()

    
    return render(request, 'menu.html')

def favorited_coffeeshop(request):
    user = request.user

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        
        favorited = {}
        
        try:
            favorited = Favorite.objects.get(user_id=user.id) 
            Favorite.delete(favorited)
        except:
            Favorite.objects.create(user_id=user)
    
    
    return redirect('perfil')
