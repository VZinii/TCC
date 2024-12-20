from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("modulo/<int:id_modulo>/", views.modulo, name='modulo'),
    path("capitulo/<int:id_capitulo>/", views.capitulo, name='capitulo'),
    path("secao/<int:id_secao>/<int:id_atividade>/", views.secao, name='secao'),
]