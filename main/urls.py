from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("modulo/<int:id_modulo>/", views.modulo, name='modulo'),
    path("modulo/<int:id_modulo>/capitulo/<int:id_capitulo>/", views.capitulo, name='capitulo'),
    path("modulo/<int:id_modulo>/capitulo/<int:id_capitulo>/secao/<int:id_secao>/", views.secao, name='secao'),
    path("modulo/<int:id_modulo>/capitulo/<int:id_capitulo>/secao/<int:id_secao>/checar", views.checar, name='checar'),
    path("removeVida/", views.removeVida, name='removeVida'),
    path("obterVidas/", views.obterVidas, name='obterVidas'),
    path("obterOuro/", views.obterOuro, name='obterOuro'),
    path("comprarVida/", views.comprarVida, name='comprarVida'),
    path("perfil/", views.perfil, name='perfil'),
    path("missoes/", views.missoes, name='missoes'),
    path("loja/", views.loja, name='loja'),
    path("amigos/", views.amigos, name='amigos'),
    path("fazerUpload/", views.fazerUpload, name='fazerUpload'),
]