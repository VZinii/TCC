from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Modulo, Capitulo, Secao, AtividadeVideoFrase, AtividadeVerdadeiroOuFalso, AtividadeEscolhaCerta, AtividadeOrdenarPalavras

@login_required(login_url="/auth/login")
def home(request):

    modulos = Modulo.objects.all().values()

    template = loader.get_template('home.html')

    context = {
        'modulos': modulos
    }

    return HttpResponse(template.render(context, request))

# @login_required(login_url="/auth/login")
# def detalhes_modulo(request, id_modulo): 

#     modulo = get_object_or_404(Modulo, numero=id_modulo)

#     modulo_obj = {
#         'nome': modulo.nome,
#         'numero': modulo.numero,
#     }

#     return JsonResponse(modulo_obj, safe=False)

@login_required(login_url="/auth/login")
def modulo(request, id_modulo):

    modulo = get_object_or_404(Modulo, numero=id_modulo)

    # Pegando todos os capitulos daquele módulo:
    capitulos = Capitulo.objects.filter(modulo=modulo)

    context = {
        'capitulos': capitulos,
        'modulo': modulo,
    }

    return render(request, 'modulo.html', context)

@login_required(login_url="/auth/login")
def capitulo(request, id_capitulo):

    print(user.name, 'teste')
    #Pegar o módulo também
    capitulo = get_object_or_404(Capitulo, numero=id_capitulo)

    # Pegando todos as seções daquele capitulo:
    secoes = Secao.objects.filter(capitulo=capitulo)

    context = {
        'secoes': secoes,
        'capitulo': capitulo,
    }

    return render(request, 'capitulo.html', context)

@login_required(login_url="/auth/login")
def secao(request, id_secao, id_atividade):

    secao = get_object_or_404(Secao, numero=id_secao)

    # Acabou essa seção, pode liberar a próxima seção
    if id_atividade == 4:

        proximaSecao = get_object_or_404(Secao, numero=id_secao+1)

        proximaSecao.liberada = True

        proximaSecao.save()

        return redirect('capitulo', secao.capitulo.numero)

    
    # Descobrir uma maneira melhor de organizar isso (Tá muito engessado, herança talvez? Uma busca em SQL usando JOIN?)
    if id_atividade == 1: # É uma de múltipla escolha
        atividade = get_object_or_404(AtividadeEscolhaCerta, secao=secao)
        template = "escolhaCerta.html"
    elif id_atividade == 2:
        atividade = get_object_or_404(AtividadeVerdadeiroOuFalso, secao=secao)
        template = "verdadeiroOuFalso.html"
    elif id_atividade == 3:
        atividade = get_object_or_404(AtividadeOrdenarPalavras, secao=secao)
        template = "ordenarPalavras.html"
    else:
        atividade = get_object_or_404(AtividadeVideoFrase, secao=secao)
        template = "traduzir.html"

    if request.method == "GET":

        palavras = []
        # Se for uma atividade de ordenar palavras, envio um vetor com as palavras para o context:
        if id_atividade == 3: 
            palavras = atividade.palavras.split()

        context = {
            'atividade': atividade,
            'palavras': palavras,
            'secao': secao,
        }
        
        return render(request, template, context)
    
    else:

        resposta = request.POST.get('resposta').rstrip() # Right Strip === Trims just the right spaces

        print(resposta, atividade.resposta)

        if resposta == atividade.resposta:
            id_atividade += 1


        return redirect('secao', id_secao, id_atividade)
