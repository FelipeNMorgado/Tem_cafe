from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('cadastro/', views.cadastro, name='cadastro'),
    # Outras URLs podem ser adicionadas aqui
]


urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('perfil/', views.perfil, name='perfilc'),
    # Outras URLs podem ser adicionadas aqui
]