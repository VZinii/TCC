from django.db import models
from django.core.validators import FileExtensionValidator

class Modulo(models.Model):
    numero = models.IntegerField(default=999)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="null")
    video_explicativo = models.FileField(upload_to='uploads/videos/modulos', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    thumbnail = models.FileField(upload_to='uploads/thumbnails/modulos', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)
    liberado = models.CharField(max_length=255, default="disabled", null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"

class Capitulo(models.Model):
    numero = models.IntegerField(default=999)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="null")
    video_explicativo = models.FileField(upload_to='uploads/videos/capitulos', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    thumbnail = models.FileField(upload_to='uploads/thumbnails/capitulos', validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], null=True, blank=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    liberado = models.CharField(max_length=255, default="disabled", null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"

class Secao(models.Model):
    numero = models.IntegerField(default=999)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, default="null")
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    liberada = models.CharField(max_length=255, default="disabled", null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome}"

class AtividadeVideoFrase(models.Model):
    numero = models.IntegerField(default=999)
    #xp = models.IntegerField()
    video_frase = models.FileField(upload_to='uploads/videos/atividades', validators = [FileExtensionValidator(allowed_extensions=['mp4'])] )
    resposta = models.CharField(max_length=255)
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)