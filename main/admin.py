from django.contrib import admin
from .models import Modulo, Capitulo, Secao, AtividadeVideoFrase, AtividadeVerdadeiroOuFalso, AtividadeOrdenarPalavras, AtividadeEscolhaCerta

class ModuloAdmin(admin.ModelAdmin):
    list_display = (["nome"])
    search_fields = ("numero", "nome")
    list_filter = ("numero", "nome")

class CapituloAdmin(admin.ModelAdmin):
    list_display = (["numero", "nome", "descricao", "modulo", "liberado"])

class SecaoAdmin(admin.ModelAdmin):
    list_display = (["numero"])

class AtividadeVideoFraseAdmin(admin.ModelAdmin):
    list_display = (["id"])

class AtividadeVerdadeiroOuFalsoAdmin(admin.ModelAdmin):
    list_display = (["id"])

class AtividadeOrdenarPalavrasAdmin(admin.ModelAdmin):
    list_display = (["id"])

class AtividadeEscolhaCertaAdmin(admin.ModelAdmin):
    list_display = (["id"])

admin.site.register(Modulo, ModuloAdmin)

admin.site.register(Capitulo, CapituloAdmin)

admin.site.register(Secao, SecaoAdmin)

admin.site.register(AtividadeVideoFrase, AtividadeVideoFraseAdmin)

admin.site.register(AtividadeVerdadeiroOuFalso, AtividadeVerdadeiroOuFalsoAdmin)

admin.site.register(AtividadeOrdenarPalavras, AtividadeOrdenarPalavrasAdmin)

admin.site.register(AtividadeEscolhaCerta, AtividadeEscolhaCertaAdmin)