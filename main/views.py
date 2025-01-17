from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Modulo, Capitulo, Secao, ProgressoUsuarioModulos, ProgressoUsuarioCapitulos, ProgressoUsuarioSecoes, AtividadeVideoFrase, AtividadeVerdadeiroOuFalso, AtividadeEscolhaCerta, AtividadeOrdenarPalavras
from django.core import serializers
from django.forms.models import model_to_dict
import json
from django.db.models import OuterRef, Subquery


@login_required(login_url="/auth/login")
def home(request):

    progressosNosModulos = obterProgressosModulos(request.user)

    modulos = Modulo.objects.all()

    for i, modulo in enumerate(modulos):

        modulo.progresso = progressosNosModulos[i]
        modulo.save()

    # Fazendo um Join das duas tabelas e criando uma com a tag liberado ou não
    modulos_com_progresso = Modulo.objects.annotate(
    liberado=Subquery(
            ProgressoUsuarioModulos.objects.filter(
                usuario=request.user,
                modulo=OuterRef('pk')
            ).values('liberado')[:1]
        )
    ).values('id', 'numero', 'nome', 'descricao', 'video_explicativo', 'thumbnail', 'progresso', 'liberado')


    context = {
        'modulos': modulos_com_progresso,
        'usuario': request.user,
        'vidas': request.user.perfil.vidas,
    }

    return render(request, 'home.html', context)


@login_required(login_url="/auth/login")
def modulo(request, id_modulo):

    modulo = get_object_or_404(Modulo, numero=id_modulo)

    progressoNoModulo = ProgressoUsuarioModulos.objects.get(usuario=request.user, modulo=modulo)

    if not(progressoNoModulo.liberado):
        return redirect('home')

    progressosNosCapitulos = obterProgressosCapitulos(request.user, modulo)

    capitulos = Capitulo.objects.filter(modulo=modulo)

    for i, capitulo in enumerate(capitulos):

        capitulo.progresso = progressosNosCapitulos[i]
        capitulo.save()

    # Fazendo um Join das duas tabelas e criando uma com a tag liberado ou não
    capitulos_com_progresso = Capitulo.objects.filter(modulo=modulo).annotate(
    liberado=Subquery(
            ProgressoUsuarioCapitulos.objects.filter(
                usuario=request.user,
                capitulo=OuterRef('pk')
            ).values('liberado')[:1]
        )
    ).values('id', 'numero', 'nome', 'descricao', 'video_explicativo', 'thumbnail', 'progresso', 'liberado')


    context = {
        'capitulos': capitulos_com_progresso,
        'modulo': modulo,
        'vidas': request.user.perfil.vidas,
    }

    return render(request, 'modulo.html', context)

@login_required(login_url="/auth/login")
def capitulo(request, id_modulo, id_capitulo):

    #Pegar o módulo atual
    modulo = get_object_or_404(Modulo, numero=id_modulo)

    #Pegar o capítulo também
    capitulo = get_object_or_404(Capitulo, numero=id_capitulo, modulo=modulo)

    progressoNoCapitulo = ProgressoUsuarioCapitulos.objects.get(usuario=request.user, capitulo=capitulo)

    if not(progressoNoCapitulo.liberado):
        return redirect('modulo', modulo.numero)

    # Fazendo um Join das tabelas Secao e ProgressoUsuarioSecoes e criando uma nova com o campo Liberada
    secoes_com_progresso = Secao.objects.filter(capitulo=capitulo).annotate(
    liberada=Subquery(
            ProgressoUsuarioSecoes.objects.filter(
                usuario=request.user,
                secao=OuterRef('pk')
            ).values('liberado')[:1]
        )
    ).values('id', 'numero', 'xp', 'ouro', 'ehTeste', 'liberada')

    context = {
        'secoes': secoes_com_progresso,
        'capitulo': capitulo,
        'modulo': modulo,
        'vidas': request.user.perfil.vidas,
    }

    return render(request, 'capitulo.html', context)


@login_required(login_url="/auth/login")
def secao(request, id_modulo, id_capitulo, id_secao):

    # Pegar o módulo atual
    modulo = get_object_or_404(Modulo, numero=id_modulo)

    # Pegar o capítulo atual desse modulo
    capitulo = get_object_or_404(Capitulo, numero=id_capitulo, modulo=modulo)

    # Pegar a seção atual desse capítulo
    secao = get_object_or_404(Secao, numero=id_secao, capitulo=capitulo)

    progressoNaSecao = ProgressoUsuarioSecoes.objects.get(usuario=request.user, secao=secao)

    if not(progressoNaSecao.liberado):
        return redirect('capitulo', modulo.numero, capitulo.numero)

    id_atividade = secao.atividadeAtual

    progressoAtual = obterProgresso(id_secao, id_atividade, id_capitulo, id_modulo)

    if progressoAtual != 0: # Chegou ao fim de alguma seção
        # Reseto o progresso da seção atual
        secao.atividadeAtual = 1
        secao.save()

    if progressoAtual == 1: # Acabou o curso
        return redirect('home')
  
    if progressoAtual == 2: # Acabou o Módulo
        # Pega o próximo módulo
        proximoModulo = get_object_or_404(Modulo, numero=id_modulo+1)
        # Pega o progresso do próximo módulo
        progressoProximoModulo = ProgressoUsuarioModulos.objects.get(usuario=request.user, modulo=proximoModulo)
        # Recebe o prêmio
        recebePremio(request.user, secao, progressoProximoModulo)
        # Libera o próximo módulo
        progressoProximoModulo.liberado = True
        # Libera o primeiro capítulo do próximo módulo
        primeiroCapitulo = Capitulo.objects.get(modulo=proximoModulo, numero=1)
        progressoPrimeiroCapitulo = ProgressoUsuarioCapitulos.objects.get(usuario=request.user, capitulo=primeiroCapitulo)
        progressoPrimeiroCapitulo.liberado = True
        # Libera a primeira seção do primeiro capítulo
        primeiraSecao = Secao.objects.get(capitulo=primeiroCapitulo, numero=1)
        progressoPrimeiraSecao = ProgressoUsuarioSecoes.objects.get(usuario=request.user, secao=primeiraSecao)
        progressoPrimeiraSecao.liberado = True
        # Atualiza o banco de dados
        progressoProximoModulo.save()
        progressoPrimeiroCapitulo.save()
        progressoPrimeiraSecao.save()

        return redirect('home')

    if progressoAtual == 3: # Acabou o Capítulo
        # Pega o próximo capítulo
        proximoCapitulo = get_object_or_404(Capitulo, numero=id_capitulo+1, modulo=modulo)
        # Pega o progresso do próximo capítulo
        progressoProximoCapitulo = ProgressoUsuarioCapitulos.objects.get(usuario=request.user, capitulo=proximoCapitulo)
        # Recebe o prêmio
        recebePremio(request.user, secao, progressoProximoCapitulo)
        # Libera o próximo capítulo
        progressoProximoCapitulo.liberado = True
        # Libera a primeira seção do próximo capítulo
        # Libera a primeira seção do primeiro capítulo
        primeiraSecao = Secao.objects.get(capitulo=proximoCapitulo, numero=1)
        progressoPrimeiraSecao = ProgressoUsuarioSecoes.objects.get(usuario=request.user, secao=primeiraSecao)
        progressoPrimeiraSecao.liberado = True

        # Atualizando o Banco de Dados
        progressoProximoCapitulo.save()
        progressoPrimeiraSecao.save()

        return redirect('modulo', id_modulo)

    if progressoAtual == 4: # Acabou a seção
        # Pega a próxima seção
        proximaSecao = get_object_or_404(Secao, numero=id_secao+1, capitulo=capitulo)
        # Pega o progresso da proxima seção
        progressoProximaSecao = ProgressoUsuarioSecoes.objects.get(usuario=request.user, secao=proximaSecao)
        # Recebe o prêmio
        recebePremio(request.user, secao, progressoProximaSecao)
        # Liberou a próxima seção
        progressoProximaSecao.liberado = True
        # Atualizando o Banco de Dados
        progressoProximaSecao.save()

        return redirect('capitulo', id_modulo, id_capitulo)

    if id_secao % 3 == 1: # É uma de múltipla escolha
        atividade = get_object_or_404(AtividadeEscolhaCerta, secao=secao, numero=id_atividade)
        template = "escolhaCerta.html"
    elif id_secao % 3 == 2:
        atividade = get_object_or_404(AtividadeVerdadeiroOuFalso, secao=secao, numero=id_atividade)
        template = "verdadeiroOuFalso.html"
    elif id_secao % 3 == 0:
        atividade = get_object_or_404(AtividadeOrdenarPalavras, secao=secao, numero=id_atividade)
        template = "ordenarPalavras.html"
    else:
        atividade = get_object_or_404(AtividadeVideoFrase, secao=secao, numero=id_atividade)
        template = "traduzir.html"

    if request.method == "GET":

        palavras = []
        # Se for uma atividade de ordenar palavras, envio um vetor com as palavras para o context:
        if id_secao % 3 == 0: 
            palavras = atividade.palavras.split()
        
        # Mostrar a quantidade de vidas durante os exercícios
        vidas = []

        for i in range(request.user.perfil.vidas):
            vidas.append('1')

        context = {
            'atividade': atividade,
            'palavras': palavras,
            'secao': secao,
            'modulo': modulo,
            'capitulo': capitulo,
            'vidas': vidas,
        }

        return render(request, template, context)
    
    else:

        # Não entra mais aqui
        return redirect('secao', id_modulo, id_capitulo, id_secao)

def checar(request, id_modulo, id_capitulo, id_secao):
    
    # Pegar o módulo atual
    modulo = get_object_or_404(Modulo, numero=id_modulo)

    # Pegar o capítulo atual desse modulo
    capitulo = get_object_or_404(Capitulo, numero=id_capitulo, modulo=modulo)

    # Pegar a seção atual desse capítulo
    secao = get_object_or_404(Secao, numero=id_secao, capitulo=capitulo)

    acertou = False

    id_atividade = secao.atividadeAtual

    if request.method == "POST":

        if id_secao % 3 == 1: # É uma de múltipla escolha
            atividade = get_object_or_404(AtividadeEscolhaCerta, secao=secao, numero=id_atividade)
        elif id_secao % 3 == 2:
            atividade = get_object_or_404(AtividadeVerdadeiroOuFalso, secao=secao, numero=id_atividade)
        elif id_secao % 3 == 0:
            atividade = get_object_or_404(AtividadeOrdenarPalavras, secao=secao, numero=id_atividade)
        else:
            atividade = get_object_or_404(AtividadeVideoFrase, secao=secao, numero=id_atividade)

        resposta = request.POST.get('resposta').rstrip() # Right Strip === Trims just the right spaces

        if resposta == atividade.resposta:
            secao.atividadeAtual += 1
            secao.save()
            acertou = True
    
    return JsonResponse({
        "acertou": acertou,
        "id_modulo": modulo.numero, 
        "id_capitulo": capitulo.numero, 
        "id_secao": secao.numero,
        "resposta_correta": atividade.resposta,
    })

def removeVida(request):

    usuario = request.user

    if ( usuario.perfil.vidas > 0 ):
        usuario.perfil.vidas -= 1
        usuario.save()
        status = "sucesso"
        mensagem = "vida removida"
    else:
        status = "erro"
        mensagem = "jogador sem vida"

    return JsonResponse({"status": status, "mensagem": mensagem})

def obterVidas(request):

    return JsonResponse({"vidas": request.user.perfil.vidas})

def obterOuro(request):

    return JsonResponse({"ouro": request.user.perfil.ouro})

def comprarVida(request):

    usuario = request.user
    
    status = "erro"

    if ( usuario.perfil.ouro < 1000 ):
        mensagem = "usuario não possui ouro suficiente"
    elif ( usuario.perfil.vidas >= 10 ):
        mensagem = "usuario atingiu o limite de vidas"
    else:
        usuario.perfil.vidas += 1
        usuario.perfil.ouro -= 1000
        usuario.save()
        status = "sucesso"
        mensagem = "vida comprada com sucesso"

    return JsonResponse({"status": status, "mensagem": mensagem, "vidas": usuario.perfil.vidas})

def perfil(request):

    if request.method == "GET":

        # Verificando a porcentagem de módulos concluídos:
        progressoModulos = ProgressoUsuarioModulos.objects.filter(usuario=request.user)
        progressoCapitulos = ProgressoUsuarioCapitulos.objects.filter(usuario=request.user)
        progressoSecoes = ProgressoUsuarioSecoes.objects.filter(usuario=request.user)
        
        porcentagemModulos = obterPorcentagemProgresso(progressoModulos)
        porcentagemCapitulos = obterPorcentagemProgresso(progressoCapitulos)
        porcentagemSecoes = obterPorcentagemProgresso(progressoSecoes)

        rotulos = ['Módulos', 'Capítulos', 'Seções']
        dados = [porcentagemModulos, porcentagemCapitulos, porcentagemSecoes]

        context = {
            'teste': "teste1",
            'usuario': request.user,
            'rotulos': rotulos,
            'dados': dados,
        }

        return render(request, "perfil.html", context)

    else:

        novaBio = request.POST.get('bioPerfil') # Right Strip === Trims just the right spaces

        usuarioAtual = request.user

        usuarioAtual.perfil.bio = novaBio

        usuarioAtual.save()

        return redirect('perfil')
    
def missoes(request):

    context = {}

    return render(request, "missoes.html", context)

def loja(request):

    context = {
        'usuario': request.user,
    }

    return render(request, "loja.html", context)

def amigos(request):

    context = {}

    return render(request, "amigos.html", context)

def configuracoes(request):

    context = {}

    return render(request, "configuracoes.html", context)

# Função Auxiliar da view Capítulo
def obterProgressosCapitulos(usuario, modulo):

    progressos = []

    capitulosDoModulo = Capitulo.objects.filter(modulo=modulo)

    quantidadeItensLiberados = 0
    totalItens = 0
    
    for capitulo in capitulosDoModulo:

        secoesDoCapitulo = Secao.objects.filter(capitulo=capitulo)

        for secao in secoesDoCapitulo:

            progressoDaSecao = ProgressoUsuarioSecoes.objects.get(usuario=usuario, secao=secao)

            if progressoDaSecao.liberado:

                quantidadeItensLiberados += 1
            
            totalItens += 1
        
        progressos.append(int(100 * quantidadeItensLiberados / totalItens))

        quantidadeItensLiberados = 0
        totalItens = 0

    return progressos

# Função Auxiliar da view Modulo
def obterProgressosModulos(usuario):

    progressos = []

    quantidadeItensLiberados = 0
    totalItens = 0

    modulos = Modulo.objects.all()

    for modulo in modulos:

        capitulosDoModulo = Capitulo.objects.filter(modulo=modulo)

        for capitulo in capitulosDoModulo:

            progressoCapitulo = ProgressoUsuarioCapitulos.objects.get(usuario=usuario, capitulo=capitulo)

            if progressoCapitulo.liberado:

                secoesDoCapitulo = Secao.objects.filter(capitulo=capitulo)

                for secao in secoesDoCapitulo:

                    progressoSecao = ProgressoUsuarioSecoes.objects.get(usuario=usuario, secao=secao)

                    if progressoSecao.liberado:

                        quantidadeItensLiberados += 1
            
            # Quantidade de seções por capítulo
            totalItens += Secao.objects.filter(capitulo=capitulo).count()
        
        progressos.append(int(100 * quantidadeItensLiberados / totalItens))

        quantidadeItensLiberados = 0
        totalItens = 0

    return progressos

# Função Auxiliar da view Seção
def obterProgresso(id_secao, id_atividade, id_capitulo, id_modulo):
    # Números que representam o que progresso atual, para melhorar a legibilidade
    # Eles deverão sofrer alteração caso o conteúdo do curso aumente.
    # Por exemplo: atualmente o curso tem dois capítulos por módulo, por isso quando
    # o id_capitulo == 2, o usuário passa de módulo.
    if id_modulo == 3 and id_capitulo == 2 and id_secao == 3 and id_atividade == 4:
        return 1 # Significa que acabou o curso
    elif id_capitulo == 2 and id_secao == 3 and id_atividade == 4:
        return 2 # Passou de Módulo
    elif id_secao == 3 and id_atividade == 4:
        return 3 # Passou de Capítulo
    elif id_atividade == 4:
        return 4 # Passou de seção
    else:
        return 0

# Função Auxiliar da view Seção
def recebePremio(usuario, secao, proximaParte):
    # Se a próxima parte estiver sendo liberada pela primeira vez, recebe o prêmio da seção atual:
    if not(proximaParte.liberado):
        usuario.perfil.xp += secao.xp
        usuario.perfil.ouro += secao.ouro
        usuario.save()

# Função auxiliar da view de perfil
def obterPorcentagemProgresso(conjunto):

    if len(conjunto) > 0:

        porcentagem = 0

        for item in conjunto:
            if item.liberado:
                porcentagem += 1
        
        return round(porcentagem * 100 / len(conjunto))

    return 0
