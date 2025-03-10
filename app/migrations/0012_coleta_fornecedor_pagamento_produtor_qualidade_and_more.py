# Generated by Django 5.1.6 on 2025-02-19 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_colaborador_fluxocaixa_medicamento_produto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('quantidade_litros', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('contato', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pagamento', models.CharField(choices=[('Pix', 'Pix'), ('Boleto', 'Boleto'), ('Transferência', 'Transferência')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('fazenda', models.CharField(max_length=150)),
                ('localizacao', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Qualidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gordura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('proteina', models.DecimalField(decimal_places=2, max_digits=5)),
                ('contagem_bacteriana', models.IntegerField()),
                ('status', models.CharField(choices=[('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motorista', models.CharField(max_length=100)),
                ('placa_veiculo', models.CharField(max_length=20)),
                ('data_envio', models.DateTimeField()),
                ('data_entrega', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateTimeField(auto_now_add=True)),
                ('quantidade_litros', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fornecedor')),
            ],
        ),
        migrations.DeleteModel(
            name='Colaborador',
        ),
        migrations.DeleteModel(
            name='FluxoCaixa',
        ),
        migrations.DeleteModel(
            name='Medicamento',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.AddField(
            model_name='pagamento',
            name='produtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produtor'),
        ),
        migrations.AddField(
            model_name='coleta',
            name='produtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produtor'),
        ),
        migrations.AddField(
            model_name='qualidade',
            name='coleta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.coleta'),
        ),
        migrations.AddField(
            model_name='transporte',
            name='venda',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.venda'),
        ),
    ]
