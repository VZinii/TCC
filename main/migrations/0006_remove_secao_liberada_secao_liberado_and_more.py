# Generated by Django 5.1.1 on 2024-11-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_capitulo_liberado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secao',
            name='liberada',
        ),
        migrations.AddField(
            model_name='secao',
            name='liberado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='liberado',
            field=models.BooleanField(default=False),
        ),
    ]
