from django.contrib import admin
from .models import Modulo, Capitulo, Secao, ProgressoUsuarioModulos, ProgressoUsuarioCapitulos, ProgressoUsuarioSecoes, AtividadeVideoFrase, AtividadeVerdadeiroOuFalso, AtividadeOrdenarPalavras, AtividadeEscolhaCerta

class ModuloAdmin(admin.ModelAdmin):
    list_display = (["nome"])
    search_fields = ("numero", "nome")
    list_filter = ("numero", "nome")

class CapituloAdmin(admin.ModelAdmin):
    list_display = (["numero", "nome", "descricao", "modulo"])

class SecaoAdmin(admin.ModelAdmin):
    list_display = (["numero", "capitulo", "xp", "ouro", "ehTeste"])

class ProgressoUsuarioModulosAdmin(admin.ModelAdmin):
    list_display = (["usuario"])

class ProgressoUsuarioCapitulosAdmin(admin.ModelAdmin):
    list_display = (["usuario"])

class ProgressoUsuarioSecoesAdmin(admin.ModelAdmin):
    list_display = (["usuario"])

class AtividadeVideoFraseAdmin(admin.ModelAdmin):
    list_display = (["numero", "secao", "resposta"])

class AtividadeVerdadeiroOuFalsoAdmin(admin.ModelAdmin):
    list_display = (["numero", "secao", "resposta"])

class AtividadeOrdenarPalavrasAdmin(admin.ModelAdmin):
    list_display = (["numero", "secao", "resposta"])

class AtividadeEscolhaCertaAdmin(admin.ModelAdmin):
    list_display = (["numero", "secao", "resposta"])

admin.site.register(Modulo, ModuloAdmin)

admin.site.register(Capitulo, CapituloAdmin)

admin.site.register(Secao, SecaoAdmin)

admin.site.register(ProgressoUsuarioModulos, ProgressoUsuarioModulosAdmin)

admin.site.register(ProgressoUsuarioCapitulos, ProgressoUsuarioCapitulosAdmin)

admin.site.register(ProgressoUsuarioSecoes, ProgressoUsuarioSecoesAdmin)

admin.site.register(AtividadeVideoFrase, AtividadeVideoFraseAdmin)

admin.site.register(AtividadeVerdadeiroOuFalso, AtividadeVerdadeiroOuFalsoAdmin)

admin.site.register(AtividadeOrdenarPalavras, AtividadeOrdenarPalavrasAdmin)

admin.site.register(AtividadeEscolhaCerta, AtividadeEscolhaCertaAdmin)