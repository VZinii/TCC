from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    context = {
        "nome": "José Silva",
        "idade": 30,
        "email": "jose.silva@email.com",
        "telefone": "3333-1234"
    }
    return HttpResponse(template.render(context, request))