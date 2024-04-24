from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil/', views.perfil, name='perfilc'),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
]