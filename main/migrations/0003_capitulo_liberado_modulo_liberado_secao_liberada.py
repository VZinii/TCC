# Generated by Django 5.1.1 on 2024-10-31 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_atividadevideofrase_numero_capitulo_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulo',
            name='liberado',
            field=models.CharField(default='disabled', max_length=255),
        ),
        migrations.AddField(
            model_name='modulo',
            name='liberado',
            field=models.CharField(default='disabled', max_length=255),
        ),
        migrations.AddField(
            model_name='secao',
            name='liberada',
            field=models.CharField(default='disabled', max_length=255),
        ),
    ]
