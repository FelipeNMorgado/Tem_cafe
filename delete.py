import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tem_cafe.settings')  
django.setup()

from django.contrib.auth.models import User
from Ctem_cafe.models import Cadastro2

User.objects.all().delete()
Cadastro2.objects.all().delete()