from django.urls import path
from . import views


urlpatterns = [
    path('', views.cadastro_cliente, name='cadastro_cliente'),  # Rota para a página inicial
    
    path('cadastro/', views.cadastro, name='cadastro'),
    
    path('perfil/', views.perfil, name='perfil'),
    
    path('menu/', views.menu, name='menu'),
    
    path('like/', views.favorited_coffeeshop, name="favorited_coffeeshop"),
    
    path('login', views.login,name='login'),

]

