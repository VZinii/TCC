from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Modulo

@login_required(login_url="/auth/login")
def home(request):

    modulos = Modulo.objects.all().values()

    template = loader.get_template('home.html')

    context = {
        'modulos': modulos
    }

    return HttpResponse(template.render(context, request))

@login_required(login_url="/auth/login")
def modulo(request):
    return HttpResponse('teste')