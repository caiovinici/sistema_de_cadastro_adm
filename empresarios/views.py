from django.shortcuts import render, redirect
from .models import Empresas # importando class do models empresarios/
from django.contrib import messages
from django.contrib.messages import constants



def cadastrar_empresa(request):
    # validação de segurança
    if not request.user.is_authenticated: # verificando se user está logado 
        return redirect('/usuarios/logar')
    #
    if request.method == "GET":
        return render(request, 'cadastrar_empresa.html', {'tempo_existencia': Empresas.tempo_existencia_choices, 'areas': Empresas.area_choices })
    #
    elif request.method == "POST":
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        site = request.POST.get('site')
        tempo_existencia = request.POST.get('tempo_existencia')
        descricao = request.POST.get('descricao')
        data_final = request.POST.get('data_final')
        percentual_equity = request.POST.get('percentual_equity')
        estagio = request.POST.get('estagio')
        area = request.POST.get('area')
        publico_alvo = request.POST.get('publico_alvo')
        valor = request.POST.get('valor')
        pitch = request.FILES.get('pitch')
        logo = request.FILES.get('logo')
    
    # Todo: Realizar validação de campos
    
    try:
        empresa = Empresas(
            user=request.user, # pegando usuario que cadastro a empresa
            nome=nome,
            cnpj=cnpj,
            site=site,
            tempo_existencia=tempo_existencia,
            descricao=descricao,
            data_final_captacao=data_final,
            percentual_equity=percentual_equity,
            estagio=estagio,
            area=area,
            publico_alvo=publico_alvo,
            valor=valor,
            pitch=pitch,
            logo=logo
 )
    #
        empresa.save()
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno no sistema.')
        return redirect('/empresarios/cadastrar_empresa')
    #
    messages.add_message(request, constants.SUCCESS, 'Empresa criada com sucesso')
    return redirect('/empresarios/cadastrar_empresa')
               
      
        # print(tempo_existencia, estagio, area) = recebendo dados do campo

''' 
passando valor do back-end para o front = 'GET'
 x = 1
    return render(request, 'cadastrar_empresa.html', {'valor': x})
'''

def listar_empresas(request):
    if not request.user.is_authenticated: # verificando se user está logado 
        return redirect('/usuarios/logar')
    
    if request.method == 'GET':
      
        # request.user()= usuario logado
        # filtrando as empresas do usuario logado
        empresas = Empresas.objects.filter(user=request.user)
        
        return render(request, 'listar_empresas.html', {'empresas': empresas})#{} dict enviando dados ao html
