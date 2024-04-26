from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ctem_cafe.urls')),  # Inclui as URLs do aplicativo Ctem_cafe
    # Outras URLs do projeto podem ser definidas aqui
]