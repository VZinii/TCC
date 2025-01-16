# Configurando o UNFOLD:
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
# Configuração normal:
from django.contrib import admin
from .models import Modulo, Capitulo, Secao, ProgressoUsuarioModulos, ProgressoUsuarioCapitulos, ProgressoUsuarioSecoes, AtividadeVideoFrase, AtividadeVerdadeiroOuFalso, AtividadeOrdenarPalavras, AtividadeEscolhaCerta

# Parâmetro => Com UNFOLD = ModelAdmin | Sem UNFOLD = admin.ModelAdmin
class ModuloAdmin(ModelAdmin):
    list_display = (["nome"])
    search_fields = ("numero", "nome")
    list_filter = ("numero", "nome")

class CapituloAdmin(ModelAdmin):
    list_display = (["numero", "nome", "descricao", "modulo"])

class SecaoAdmin(ModelAdmin):
    list_display = (["numero", "capitulo", "xp", "ouro", "ehTeste"])

class ProgressoUsuarioModulosAdmin(ModelAdmin):
    list_display = (["usuario"])

class ProgressoUsuarioCapitulosAdmin(ModelAdmin):
    list_display = (["usuario"])

class ProgressoUsuarioSecoesAdmin(ModelAdmin):
    list_display = (["usuario"])

class AtividadeVideoFraseAdmin(ModelAdmin):
    list_display = (["numero", "secao", "resposta"])

class AtividadeVerdadeiroOuFalsoAdmin(ModelAdmin):
    list_display = (["numero", "secao", "resposta"])

class AtividadeOrdenarPalavrasAdmin(ModelAdmin):
    list_display = (["numero", "secao", "resposta"])

class AtividadeEscolhaCertaAdmin(ModelAdmin):
    list_display = (["numero", "secao", "resposta"])

class ConfiguracaoAdmin(ModelAdmin):
    list_display = (["usuario", "tema"])

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

# Configurações para o Unfold:
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass