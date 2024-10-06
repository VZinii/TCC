from django.db import models
from django.core.validators import FileExtensionValidator

class Modulo(models.Model):
    nome = models.CharField(max_length=255)
    video_explicativo = models.FileField(upload_to='uploads/videos/modulos', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    thumbnail = models.FileField(upload_to='uploads/thumbnails/modulos', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)

class Capitulo(models.Model):
    nome = models.CharField(max_length=255)
    video_explicativo = models.FileField(upload_to='uploads/videos/capitulos', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    thumbnail = models.FileField(upload_to='uploads/thumbnails/capitulos', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)

class Secao(models.Model):
    nome = models.CharField(max_length=255)
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)

class AtividadeVideoFrase(models.Model):
    video_frase = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    resposta = models.CharField(max_length=255)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)