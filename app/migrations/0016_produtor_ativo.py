# Generated by Django 5.1.6 on 2025-02-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_coleta_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtor',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
