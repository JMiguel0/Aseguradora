# Generated by Django 3.2.3 on 2021-05-24 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Agentes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agente',
            name='ap_materno',
        ),
        migrations.RemoveField(
            model_name='agente',
            name='ap_paterno',
        ),
        migrations.RemoveField(
            model_name='agente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='agente',
            name='fecha_ingreso',
        ),
        migrations.RemoveField(
            model_name='agente',
            name='nombre',
        ),
    ]
