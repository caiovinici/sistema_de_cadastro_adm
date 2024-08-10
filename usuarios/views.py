''' LOGICA DA APLICAÇÃO: RECEBER REQUISIÇÃO HTTP E DEVOLVER UMA RESPONSE =
TEMPLATES: HTML/CSS/JS '''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def cadastro(request):
    # print(request.META)
    # return HttpResponse('Olá mundo!') # resposta HTTP
    
    if request.method == 'GET':
        return render(request, 'cadastro.html') # REDENIZA O HTML - passando caminho do HTML
    #
    elif request.method == "POST":
        # print(request.POST) # retorna username e senha registrados
        username = request.POST.get('username') # pegando informações de username
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        # confirmando senhas
        if senha != confirmar_senha:
            # msg de erros bootstrap
            messages.add_message(request, constants.ERROR, 'As senhas não coíncidem.')
            
            # REDIRECIONA CASO SENHAS TIVER DIFERENTES = PÁG CADASTRO
            return redirect('/usuarios/cadastro') # REDIRECIONA CASO SENHAS TIVER DIFERENTES
        
        # verificando tamanho da senha do usuario
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha precisa ter pelo menos 6 dígitos.')
            return redirect('/usuarios/cadastro')
        
        # verificando se usuario já existe no BD
        #                   .all() busca todo os usuarios cadastrados
        users = User.objects.filter(username=username)
        # print(users.exists())
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome.')
            return redirect('/usuarios/cadastro')
        
        # criando usuario
        user = User.objects.create_user(
            username=username,
            password=senha,
        )
        return redirect('/usuarios/logar') # URL logar ainda não existe
        
        # return HttpResponse(f'{username} - {senha} - {confirmar_senha}')
#

# criando url logar
def logar(request):
    if request.method == 'GET': # diferenciando o request de GET E POST
        return render(request, 'logar.html')
    # return HttpResponse('TESTE') # TESTANDO URL 
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha =  request.POST.get('senha')
        
        # recebe func do usuario, e procura se existe algum usuario com o username e senha ativo
        user = auth.authenticate(request, username=username, password=senha) 
        # print(user)
        
        if user:
            auth.login(request, user) #.login = de fato que loga no banco de dados
            return redirect('/empresarios/cadastrar_empresa') # URL AINDA NÃO EXISTE
        messages.add_message(request, constants.ERROR, 'Usuário ou senha inválida!  ')
        # return HttpResponse('TESTE')
        return redirect('/usuarios/logar')