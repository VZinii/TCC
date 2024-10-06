# Generated by Django 5.1.1 on 2024-10-06 13:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('video_explicativo', models.FileField(upload_to='uploads/videos/modulos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='uploads/thumbnails/modulos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
            ],
        ),
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('video_explicativo', models.FileField(upload_to='uploads/videos/capitulos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='uploads/thumbnails/capitulos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modulo')),
            ],
        ),
        migrations.CreateModel(
            name='Secao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.capitulo')),
            ],
        ),
        migrations.CreateModel(
            name='AtividadeVideoFrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_frase', models.FileField(upload_to='uploads/videos/atividades', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('resposta', models.CharField(max_length=255)),
                ('secao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.secao')),
            ],
        ),
    ]
