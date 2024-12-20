# Generated by Django 5.1.1 on 2024-11-13 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_liberado_secao_liberada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secao',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='secao',
            name='nome',
        ),
        migrations.AddField(
            model_name='secao',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
