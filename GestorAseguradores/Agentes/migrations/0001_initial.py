# Generated by Django 3.2.3 on 2021-05-24 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ap_paterno', models.CharField(max_length=30)),
                ('ap_materno', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('email', models.CharField(max_length=30)),
                ('num_celular', models.CharField(max_length=10)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('colonia', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('rfc', models.CharField(max_length=30)),
                ('fecha_registro', models.DateField()),
                ('status', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
