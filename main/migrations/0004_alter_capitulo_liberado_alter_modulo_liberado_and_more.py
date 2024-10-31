# Generated by Django 5.1.1 on 2024-10-31 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_capitulo_liberado_modulo_liberado_secao_liberada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='liberado',
            field=models.CharField(blank=True, default='disabled', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='modulo',
            name='liberado',
            field=models.CharField(blank=True, default='disabled', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='secao',
            name='liberada',
            field=models.CharField(blank=True, default='disabled', max_length=255, null=True),
        ),
    ]