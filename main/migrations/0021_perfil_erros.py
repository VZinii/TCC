# Generated by Django 5.1.1 on 2024-12-29 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='erros',
            field=models.IntegerField(default=0),
        ),
    ]
