# Generated by Django 5.1.6 on 2025-02-20 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_qualidade_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualidade',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
