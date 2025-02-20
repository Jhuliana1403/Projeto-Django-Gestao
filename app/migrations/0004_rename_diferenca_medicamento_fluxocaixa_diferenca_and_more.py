# Generated by Django 5.1.6 on 2025-02-18 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_diferenca_valor_fluxocaixa_diferenca_medicamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fluxocaixa',
            old_name='diferenca_medicamento',
            new_name='diferenca',
        ),
        migrations.RenameField(
            model_name='fluxocaixa',
            old_name='diferenca_produto',
            new_name='valor_total',
        ),
        migrations.RemoveField(
            model_name='fluxocaixa',
            name='valor_total_medicamentos',
        ),
        migrations.RemoveField(
            model_name='fluxocaixa',
            name='valor_total_produtos',
        ),
    ]
