# Generated by Django 3.2.3 on 2021-05-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agentes', '0005_agente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
