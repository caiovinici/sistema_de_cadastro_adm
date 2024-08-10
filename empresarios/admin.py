from django.contrib import admin
from .models import Empresas # importando a tabela do BD
# Register your models here.

# URL /ADMIN
admin.site.register(Empresas)
