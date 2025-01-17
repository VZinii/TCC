from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)
    ouro = models.IntegerField(default=0)
    bio = models.TextField(max_length=500, blank=True)
    vidas = models.IntegerField(default=5)
    erros = models.IntegerField(default=0)

# Criando sinais para que quando um User do django for criado ou alterado, automaticamente
# essas alterações sejam refletidas na tabela Perfil 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()

class Modulo(models.Model):
    numero = models.IntegerField(default=999)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="null")
    video_explicativo = models.FileField(upload_to='uploads/videos/modulos', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    thumbnail = models.FileField(upload_to='uploads/thumbnails/modulos', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)
    progresso = models.IntegerField(default=0)

    def __str__(self):
        return f"Módulo {self.numero}"

class Capitulo(models.Model):
    numero = models.IntegerField(default=999)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="null")
    video_explicativo = models.FileField(upload_to='uploads/videos/capitulos', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    thumbnail = models.FileField(upload_to='uploads/thumbnails/capitulos', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    progresso = models.IntegerField(default=0)

    def __str__(self):
        return f"Capítulo {self.numero} - {self.modulo}"

class Secao(models.Model):
    numero = models.IntegerField(default=999)
    xp = models.IntegerField(default=0)
    ouro = models.IntegerField(default=0)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    ehTeste = models.BooleanField(default=False)
    atividadeAtual = models.IntegerField(default=1)

    def __str__(self):
        return f"Seção {self.numero} - {self.capitulo}"

class AtividadeVideoFrase(models.Model):
    numero = models.IntegerField(default=999)
    video_atividade = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    resposta = models.CharField(max_length=255)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atividade {self.numero} de {self.secao}"

class AtividadeVerdadeiroOuFalso(models.Model):
    numero = models.IntegerField(default=999)
    video_atividade = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    afirmacao = models.CharField(max_length=255, default="")
    resposta = models.CharField(max_length=1)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atividade {self.numero} de {self.secao}"

class AtividadeOrdenarPalavras(models.Model):
    numero = models.IntegerField(default=999)
    video_atividade = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    palavras = models.CharField(max_length=255)
    resposta = models.CharField(max_length=255)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atividade {self.numero} de {self.secao}"

class AtividadeEscolhaCerta(models.Model):
    numero = models.IntegerField(default=999)
    video_atividade = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    resposta = models.CharField(max_length=1)
    alternativaA = models.CharField(max_length=255)
    alternativaB = models.CharField(max_length=255)
    alternativaC = models.CharField(max_length=255)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atividade {self.numero} de {self.secao}"


class ProgressoUsuarioModulos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    liberado = models.BooleanField(default=False)

    def __str__(self):
        return f"Progresso de {self.usuario} em {self.modulo}"


class ProgressoUsuarioCapitulos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    liberado = models.BooleanField(default=False)

    def __str__(self):
        return f"Progresso de {self.usuario} em {self.capitulo}"


class ProgressoUsuarioSecoes(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
    liberado = models.BooleanField(default=False)

    def __str__(self):
        return f"Progresso de {self.usuario} em {self.secao}"
    