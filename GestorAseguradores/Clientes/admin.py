from django.contrib import admin
from .models import *
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre","agente","status")

admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Poliza)
admin.site.register(Status)
admin.site.register(Tipos_Poliza)
admin.site.register(Periodos_Pago)