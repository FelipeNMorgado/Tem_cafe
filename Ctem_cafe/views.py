
from django.shortcuts import render, redirect
from .models import Cadastro
from .models import Cliente
from .models import Favorite
from django.contrib.auth import authenticate,login
from django.http.response import HttpResponse
from django.contrib.auth import login as logind

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
            concordo_termos=concordo_termos
        )
        cliente.save()

        return redirect('home')

    
def perfil(request):
    return render(request, 'visperfil.html')



def menu(request):

    

    cafeterias = []


    for cafeterias_info in Cadastro.objects.all():

        cafeterias_data = {
            'nome_loja': cafeterias_info.nome_loja,
            'bairro': cafeterias_info.bairro,
            'endereco': cafeterias_info.endereco,
            'complemento': cafeterias_info.complemento
        }

        cafeterias.append(cafeterias_data)

    context = {
        'cafeterias': cafeterias
    }



    return render(request, 'menu.html', context)


#  ------------------------EXEMPLO-----------------------------------




# ------------------------EXEMPLO-----------------------------------





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


def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    else:
        nome=request.POST.get('inputEmail4')
        Senha=request.POST.get('inputPassword4')
        
        vali=authenticate(nome_completo=nome,senha=Senha)
        if vali:
            logind(request,vali)
            return render(request,'menu.html')
        else:
           return HttpResponse('Você precisa estar logado')
        