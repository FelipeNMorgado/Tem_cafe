from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),  # Rota para a página inicial
    
    path('cadastro/', views.cadastro, name='cadastro'),
    
    path('perfil/', views.perfil, name='perfil'),
    
    path('menu/', views.menu, name='menu'),
    
    path('like/', views.favorited_coffeeshop, name="favorited_coffeeshop"),
    
    path('cadastro_cliente', views.cadastro_cliente, name='cadastro_cliente'),

]

