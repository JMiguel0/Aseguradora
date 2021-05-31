
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Agente(AbstractUser):
    
    num_celular = models.CharField(max_length=10)
    codigo_postal = models.CharField(max_length=5, null=True,default="")
    colonia = models.CharField(max_length=50, null=True,default="")
    direccion = models.CharField(max_length=30, null=True,default="")
    rfc = models.CharField(max_length=30, null=True,default="")
    status = models.CharField(max_length=30, null=True,default="")
    imagen = models.CharField(max_length=500, default="https://i1.wp.com/mundowin.com/wp-content/uploads/2020/02/fix-corrupt-user-profile-windows-pc.png?w=832&ssl=1")
    



