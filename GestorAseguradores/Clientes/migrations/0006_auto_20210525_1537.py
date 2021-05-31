# Generated by Django 3.2.3 on 2021-05-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0005_cliente_agente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo_postal',
            field=models.CharField(blank=True, default='', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='num_fijo',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rfc',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
