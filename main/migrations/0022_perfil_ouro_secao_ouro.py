# Generated by Django 5.1.1 on 2025-01-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_perfil_erros'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='ouro',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='secao',
            name='ouro',
            field=models.IntegerField(default=0),
        ),
    ]
