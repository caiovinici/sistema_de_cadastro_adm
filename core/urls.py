'''
Pasta core = corpo do API
URLS iniciais dos APIs exp: /usuarios, /empresarios




'''

from django.contrib import admin
from django.urls import path, include


urlpatterns = [ #  inicio das URLs no django
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('empresarios/', include('empresarios.urls')),
]

# include = inclui um API dentro da rota URL