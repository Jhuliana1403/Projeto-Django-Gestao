# Generated by Django 5.1.6 on 2025-02-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_colaborador_fluxocaixa_soma_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
