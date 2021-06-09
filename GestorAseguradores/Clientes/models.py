from django.db import models
from django.db.models.base import Model

from Agentes.models import Agente

# Create your models here.

class Tipos_Poliza(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Tipos_Pago(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Periodos_Pago(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Status(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Cliente (models.Model):

    nombre = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, default="")
    num_celular = models.CharField(max_length=10)
    num_fijo = models.CharField(max_length=10, null=True, blank=True, default="")
    codigo_postal = models.CharField(max_length=5, null=True, blank=True, default="")
    colonia = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    rfc = models.CharField(max_length=30, null=True, blank=True, default="")
    fecha_registro = models.DateField()
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre +" "+ self.ap_paterno

class Poliza (models.Model):
    num_poliza = models.CharField(max_length=30) 
    deducible = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    tipo_poliza = models.ForeignKey(Tipos_Poliza, on_delete=models.CASCADE)
    periodo_pago = models.ForeignKey(Periodos_Pago, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.num_poliza +", "+ self.cliente.nombre

class TiposPago (models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Prima (models.Model):
    no_prima = models.CharField(max_length=30) 
    fecha_vencimiento = models.DateField()
    prima_neta = models.CharField(max_length=30)
    comision_agente = models.CharField(max_length=30)
    total_pagar = models.CharField(max_length=30)
    ruta_comprobante = models.CharField(max_length=30, default="Hola")
    poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    tipo_pago = models.ForeignKey(TiposPago, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.no_prima