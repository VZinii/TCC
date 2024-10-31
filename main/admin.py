from django.contrib import admin
from .models import Modulo, Capitulo, Secao, AtividadeVideoFrase

class ModuloAdmin(admin.ModelAdmin):
    list_display = (["nome"])

class CapituloAdmin(admin.ModelAdmin):
    list_display = (["nome"])

class SecaoAdmin(admin.ModelAdmin):
    list_display = (["nome"])

class AtividadeVideoFraseAdmin(admin.ModelAdmin):
    list_display = (["id"])

admin.site.register(Modulo, ModuloAdmin)

admin.site.register(Capitulo, CapituloAdmin)

admin.site.register(Secao, SecaoAdmin)

admin.site.register(AtividadeVideoFrase, AtividadeVideoFraseAdmin)