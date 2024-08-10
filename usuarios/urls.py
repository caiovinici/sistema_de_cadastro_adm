''' Criando o caminho das URLS dos usuarios
exp: usuarios/login, usuarios/cadastro'''
from django.urls import path
from . import views

# criando rotas da URLs de usuarios
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'), # URL criando uma views
    path('logar/', views.logar, name='logar'), # url de logar
]
