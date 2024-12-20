from django.db import models
from django.core.validators import FileExtensionValidator

class Modulo(models.Model):
    numero = models.IntegerField(default=999)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="null")
    video_explicativo = models.FileField(upload_to='uploads/videos/modulos', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    thumbnail = models.FileField(upload_to='uploads/thumbnails/modulos', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)
    liberado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero} - {self.nome}"

class Capitulo(models.Model):
    numero = models.IntegerField(default=999)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="null")
    video_explicativo = models.FileField(upload_to='uploads/videos/capitulos', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    thumbnail = models.FileField(upload_to='uploads/thumbnails/capitulos', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    liberado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.modulo} - {self.numero} - {self.nome}"

class Secao(models.Model):
    numero = models.IntegerField(default=999)
    xp = models.IntegerField(default=0)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    liberada = models.BooleanField(default=False)
    ehTeste = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.numero}"

class AtividadeVideoFrase(models.Model):
    numero = models.IntegerField(default=999)
    video_atividade = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    resposta = models.CharField(max_length=255)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

class AtividadeVerdadeiroOuFalso(models.Model):
    numero = models.IntegerField(default=999)
    video_atividade = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    afirmacao = models.CharField(max_length=255, default="")
    resposta = models.CharField(max_length=1)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

class AtividadeOrdenarPalavras(models.Model):
    numero = models.IntegerField(default=999)
    video_atividade = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    palavras = models.CharField(max_length=255)
    resposta = models.CharField(max_length=255)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

class AtividadeEscolhaCerta(models.Model):
    numero = models.IntegerField(default=999)
    video_atividade = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    resposta = models.CharField(max_length=1)
    alternativaA = models.CharField(max_length=255)
    alternativaB = models.CharField(max_length=255)
    alternativaC = models.CharField(max_length=255)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)