import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadastro, Avaliacao3, Cliente, Favorite3, TagCafeteria3, TagUsuario
from django.contrib.auth import authenticate, login as logind
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

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
        cadastro.save()

        return redirect('home')

def cadastro_cliente(request):
    if request.method == "GET":
        return render(request, 'cadastro_cliente.html')
    elif request.method == "POST":
        nome = request.POST.get('inputFullName')
        email = request.POST.get('inputEmail4')
        senha = request.POST.get('inputPassword4')

        user = User.objects.filter(email=email).first()

        if user:
            return HttpResponse("Esse email já está cadastrado")

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return redirect('login')

@login_required
def perfil(request, nome_cafeteria):
    if request.method == 'POST':
        avaliador = request.user.username
        avaliado = nome_cafeteria
        nota = int(request.POST.get('rate'))
        Avaliacao3.objects.create(avaliador=avaliador, avaliado=avaliado, nota=nota, user=request.user)
        return JsonResponse({'status': 'success'})
    else:
        cafeteria = get_object_or_404(Cadastro, nome_loja=nome_cafeteria)
        tags = TagCafeteria3.objects.filter(user_id=request.user)
        favorited = Favorite3.objects.filter(usuario=request.user.username, cafeteria=nome_cafeteria, user_id=request.user).exists()
        return render(request, 'visperfil.html', {'cafeteria': cafeteria, 'tags': tags, 'favorited': favorited})

@login_required
@csrf_exempt
def add_tag(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cafeteria_name = data.get('post_id')  # Corrigido para pegar do JSON
        tag_name = data.get('tag')
        if tag_name:
            tag = TagCafeteria3(user_id=request.user, cafeteria=cafeteria_name, tag_name=tag_name)
            tag.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'message': 'Invalid tag name'})
    return JsonResponse({'success': False, 'message': 'Invalid request'})
   


def menu(request):
    cafeterias = Cadastro.objects.all()
    context = {'cafeterias': cafeterias}
    return render(request, 'menu.html', context)

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        name = request.POST.get('inputEmail4')
        senha = request.POST.get('inputPassword4')
        vali = authenticate(username=name, password=senha)
        if vali:
            logind(request, vali)
            return redirect('menu')
        else:
            return HttpResponse('Você precisa estar logado')


@login_required
def favorited_coffeeshop(request):
    if request.method == "POST":
        cafeteria_name = request.POST.get('post_id')
        user = request.user

        try:
            favorited = Favorite3.objects.get(usuario=user.username, cafeteria=cafeteria_name, user_id=user)
            favorited.delete()
        except Favorite3.DoesNotExist:
            Favorite3.objects.create(usuario=user.username, cafeteria=cafeteria_name, user_id=user)

        return redirect('perfil', nome_cafeteria=cafeteria_name)

    return redirect('menu')

def mapa (request):
    return render(request,'mapa.html')

    
def perfil_usuario(request):
    return render(request, 'userperfil.html', {'username': request.user.username})

@login_required
@csrf_exempt
def add_tag_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tag_name = data.get('tag')
        if tag_name:
            tag = TagUsuario(user_id=request.user, usuario=request.user.username, tag_name=tag_name)
            tag.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'message': 'Invalid tag name'})
    return JsonResponse({'success': False, 'message': 'Invalid request'})
