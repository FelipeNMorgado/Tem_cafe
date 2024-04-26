from django.contrib import admin
from .models import Favorite
from .models import Cliente
from .models import Cadastro

# Register your models here.
admin.site.register(Favorite)
admin.site.register(Cliente)
admin.site.register(Cadastro)