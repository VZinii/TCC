# Generated by Django 5.1.1 on 2024-10-31 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividadevideofrase',
            name='numero',
            field=models.IntegerField(default=999),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='descricao',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='capitulo',
            name='numero',
            field=models.IntegerField(default=999),
        ),
        migrations.AddField(
            model_name='modulo',
            name='descricao',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='modulo',
            name='numero',
            field=models.IntegerField(default=999),
        ),
        migrations.AddField(
            model_name='secao',
            name='descricao',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AddField(
            model_name='secao',
            name='numero',
            field=models.IntegerField(default=999),
        ),
    ]
