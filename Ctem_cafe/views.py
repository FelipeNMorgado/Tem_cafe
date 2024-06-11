import json
import random
from django.db.models import Count, Avg
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cadastro2, Avaliacao3, Cliente, Favorite3, TagCafeteria3, TagUsuario, Noticias
from django.contrib.auth import authenticate, login as logind
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator

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

        cadastro = Cadastro2(
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

        return redirect('login')

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
        
        avaliacoes_cafe = Avaliacao3.objects.filter(avaliado=nome_cafeteria)
        media = avaliacoes_cafe.aggregate(avg_nota=Avg('nota'))['avg_nota']
        media = round(media, 1) if media is not None else None
        
        return JsonResponse({'status': 'success'})
    else:
        cafeteria = get_object_or_404(Cadastro2, nome_loja=nome_cafeteria)
        tags = TagCafeteria3.objects.filter(cafeteria=cafeteria.nome_loja)
        favorited = Favorite3.objects.filter(usuario=request.user.username, cafeteria=nome_cafeteria, user_id=request.user).exists()
        avaliacoes_cafe = Avaliacao3.objects.filter(avaliado=nome_cafeteria)
        media = avaliacoes_cafe.aggregate(avg_nota=Avg('nota'))['avg_nota']
        media = round(media, 1) if media is not None else None
        return render(request, 'visperfil.html', {'cafeteria': cafeteria, 'tags': tags, 'favorited': favorited, 'media': media})

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

@login_required
@csrf_exempt
def remove_tag(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tag_id = data.get('tag_id')
        try:
            tag = TagCafeteria3.objects.get(id=tag_id)
            if tag.user_id == request.user:
                tag.delete()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Não autorizado'})
        except TagCafeteria3.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Tag não encontrada'})
    return JsonResponse({'success': False, 'message': 'Requisição inválida'})

def menu(request):
    cafeterias = Cadastro2.objects.all()
    user_tags = TagUsuario.objects.filter(user_id=request.user).values_list('tag_name', flat=True)
    noticias = Noticias.objects.all()

    cafeterias = Cadastro2.objects.all()
    cafes_json = serialize('json', cafeterias, fields=('nome_loja', 'endereco', 'complemento', 'cidade', 'bairro', 'estado', 'cep'))
    
    recommended_cafeterias = list(Cadastro2.objects.filter(
        nome_loja__in=TagCafeteria3.objects.filter(tag_name__in=user_tags).values_list('cafeteria', flat=True)
    ).distinct())

    if len(recommended_cafeterias) > 5:
        recommended_cafeterias = random.sample(recommended_cafeterias, 5)

    cofeeshop = Cadastro2.objects.all()

    for cafe in cofeeshop:
        avaliacoes_cafe = Avaliacao3.objects.filter(avaliado=cafe.nome_loja)
        cafe.num_avaliacoes = avaliacoes_cafe.count()
        media = avaliacoes_cafe.aggregate(avg_nota=Avg('nota'))['avg_nota']
        cafe.avg_nota = round(media, 1) if media is not None else None

    cofeeshop = sorted(cofeeshop, key=lambda x: x.avg_nota if x.avg_nota is not None else float('-inf'), reverse=True)

    limit = 5
    cofeeshop = cofeeshop[:limit]
    noticias = noticias[:limit]

    favoritos = Favorite3.objects.filter(usuario=request.user)

    # Obter os detalhes das cafeterias favoritas
    favoritas_detalhes = Cadastro2.objects.filter(nome_loja__in=[fav.cafeteria for fav in favoritos])

    # Criar uma lista de dicionários contendo os detalhes necessários para o template
    favoritos_detalhes = [
        {
            'favorito': fav,
            'cafeteria': next(cafe for cafe in favoritas_detalhes if cafe.nome_loja == fav.cafeteria)
        }
        for fav in favoritos
    ]

    context = {
        'media': cofeeshop,
        'cafeterias': cafeterias,
        'recommended_cafeterias': recommended_cafeterias,
         'cafes_json': cafes_json,
        'favoritos_detalhes': favoritos_detalhes,
        'noticias': noticias
    }

    return render(request, 'menu.html', context)



def busca(request):
    search_term = request.GET.get('search')
    filters = request.GET.getlist('filters[]')
    
    cafeterias = Cadastro2.objects.all()

    if filters:
        tag_cafeterias = TagCafeteria3.objects.filter(tag_name__in=filters).values_list('cafeteria', flat=True)
        cafeterias = cafeterias.filter(nome_loja__in=tag_cafeterias).distinct()
    
    if search_term:
        cafeterias = cafeterias.filter(nome_loja__icontains=search_term)

    context = {
        'cafeterias': cafeterias,
    }

    return render(request, 'busca.html', context)



def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        name = request.POST.get('inputEmail4')
        senha = request.POST.get('inputPassword4')
        vali = authenticate(username=name, password=senha)
        if vali:
            logind(request, vali)
            if vali.is_superuser:
                return redirect('perfil', nome_cafeteria=name)
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


def mapa(request):
    cafeterias = Cadastro2.objects.all()
    cafes_json = serialize('json', cafeterias, fields=('nome_loja', 'endereco', 'complemento', 'cidade', 'bairro', 'estado', 'cep'))
    context = {
        'cafes_json': cafes_json
    }
    return render(request, 'mapa.html', context)


    
def perfil_usuario(request):
    user_tags = TagUsuario.objects.filter(usuario=request.user)
    return render(request, 'userperfil.html', {
        'username': request.user.username,
        'user_tags': user_tags
    })

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


@login_required
@csrf_exempt
def remove_tag_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tag_id = data.get('tag_id')
        try:
            tag = TagUsuario.objects.get(id=tag_id)
            if tag.user_id == request.user:
                tag.delete()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Não autorizado'})
        except TagUsuario.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Tag não encontrada'})
    return JsonResponse({'success': False, 'message': 'Requisição inválida'})


def cadastro_cafeteria(request):
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
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return redirect('cadastro')

@method_decorator(login_required, name='dispatch')
class edit_perfil(UpdateView):
    model = Cadastro2
    fields = ['descricao', 'arq']
    template_name = 'edit_perfil.html'
    
    def get_success_url(self):
        nome_cafeteria = self.object.nome_loja
        return reverse_lazy('perfil', kwargs={'nome_cafeteria': nome_cafeteria})

    def get_object(self, queryset=None):
        nome_loja = self.kwargs.get('nome_loja')
        return get_object_or_404(Cadastro2, nome_loja=nome_loja)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editando Cadastro"
        context["botao"] = "Atualizar"
        return context


def noticias(request):
    noticias = Noticias.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})


def escrever_noticias(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        description = request.POST.get('description')
        foto = request.POST.get('foto')
        cafeteria = request.user.username

        noticia = Noticias(
            titulo=titulo,
            descricao=description,
            arq=foto,
            cafeteria=cafeteria,
            user_id=request.user
        )
        noticia.save()
        return redirect('perfil', nome_cafeteria=cafeteria)
    else:
        return render(request, 'escrever_noticias.html')


