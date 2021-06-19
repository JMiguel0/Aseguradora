from django.contrib import admin
from .models import *
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre","agente","status")

class PrimasAdmin(admin.ModelAdmin):
    list_display = ("no_prima","poliza","status")

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Poliza)
admin.site.register(Prima, PrimasAdmin)
admin.site.register(Status)
admin.site.register(TiposPago)
admin.site.register(Tipos_Poliza)
admin.site.register(Periodos_Pago)