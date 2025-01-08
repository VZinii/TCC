from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("modulo/<int:id_modulo>/", views.modulo, name='modulo'),
    path("modulo/<int:id_modulo>/capitulo/<int:id_capitulo>/", views.capitulo, name='capitulo'),
    path("modulo/<int:id_modulo>/capitulo/<int:id_capitulo>/secao/<int:id_secao>/<int:id_atividade>/", views.secao, name='secao'),
    path("perfil/", views.perfil, name='perfil'),
    path("missoes/", views.missoes, name='missoes'),
    path("loja/", views.loja, name='loja'),
    path("amigos/", views.amigos, name='amigos'),
    path("configuracoes/", views.configuracoes, name='configuracoes'),
]