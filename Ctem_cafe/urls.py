from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro_cafeteria/', views.cadastro_cafeteria, name='cadastro_cafeteria'),
    path('perfil/<str:nome_cafeteria>/', views.perfil, name='perfil'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('add_tag_usuario/', views.add_tag_usuario, name='add_tag_usuario'),
    path('favorited_coffeeshop/', views.favorited_coffeeshop, name='favorited_coffeeshop'),
    path('menu/', views.menu, name='menu'),
    path('mapa/', views.mapa, name='mapa'),
    path('busca/', views.busca, name='busca')
]
