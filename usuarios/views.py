from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth import logout as logout_django
from main.models import ProgressoUsuarioCapitulos, ProgressoUsuarioModulos, ProgressoUsuarioSecoes, Modulo, Capitulo, Secao

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(username=usuario, password=senha)

        if user:
            login_django(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Dar um jeito de criar todos os módulos, capítulos e seções para cada usuário cadastrado
        user = User.objects.filter(username=usuario).first()
        if user:
            return redirect('cadastro')
        
        # se não existir usuário com esse nome cria e salva o mesmo.
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        user.save()

        criarTabelasProgresso(user)

        return render(request, 'login.html')

def logout(request):
    logout_django(request)
    return redirect("login")

# Função para criar o conteúdo 
def criarTabelasProgresso(user):

    modulos = Modulo.objects.all()
    # Vou criar tabelas de progresso para o usuário
    for modulo in modulos:

        if modulo.numero == 1:
            liberado = True
        else:
            liberado = False

        progressoModulo = ProgressoUsuarioModulos.objects.create(usuario=user, modulo=modulo, liberado=liberado)
        progressoModulo.save()
            
        # Pega os capitulos do modulo atual:
        capitulos = Capitulo.objects.filter(modulo=modulo)
        for capitulo in capitulos:

            if capitulo.numero == 1 and capitulo.modulo.numero == 1:
                liberado = True
            else:
                liberado = False

            progressoCapitulo = ProgressoUsuarioCapitulos.objects.create(usuario=user, capitulo=capitulo, liberado=liberado)
            progressoCapitulo.save()

            # Pega as secoes desse capitulo
            secoes = Secao.objects.filter(capitulo=capitulo)
            for secao in secoes:

                if secao.numero == 1 and secao.capitulo.numero == 1 and secao.capitulo.modulo.numero == 1:
                    liberado = True
                else:
                    liberado = False

                progressoSecao = ProgressoUsuarioSecoes.objects.create(usuario=user, secao=secao, liberado=liberado)
                progressoSecao.save()