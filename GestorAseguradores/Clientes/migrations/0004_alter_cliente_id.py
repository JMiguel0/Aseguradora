# Generated by Django 3.2.3 on 2021-05-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_rename_fecha_ingreso_cliente_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
