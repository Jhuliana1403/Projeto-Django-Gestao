# Generated by Django 5.1.6 on 2025-02-17 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_inicial', models.IntegerField()),
                ('quantidade_final', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FluxoCaixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diferenca_quantidade', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.produto')),
            ],
        ),
    ]
