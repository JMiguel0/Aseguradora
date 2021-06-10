

from django.db import close_old_connections
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Clientes
def index(request):
    
    lista_clientes = Cliente.objects.filter(agente=request.user)
    return render(request, 'clientes.html', {'lista': lista_clientes})

def nuevo(request):
    cliente = ClienteForm(request.POST or None)
    if cliente.is_valid():
        instance = cliente.save(commit=False)
        instance.agente = request.user
        instance.save()
        return redirect('Clientes:index')
    return render(request, 'registro_cliente.html', {'cliente': cliente})

def editar(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('Clientes:index')
    return render(request, 'editar.html', {'form':form, 'cliente':cliente})

def detalle(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    polizas = Poliza.objects.filter(cliente = id_cliente)
    context ={
        'cliente':cliente,
        'poliza':polizas
        }
    return render(request, 'detalle.html', context)

def eliminar(request, id_cliente):
    cliente = Cliente.objects.get(id = id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('Clientes:index')
    return render(request,'eliminar.html', {'cliente':cliente})
#Pólizas 

def polizas(request):

    lista_polizas = Poliza.objects.none()
    cliente = Cliente.objects.filter(agente = request.user)
    for usuario in cliente:
        lista_polizas  |= Poliza.objects.filter(cliente = usuario)
    lista = list(lista_polizas)
    return render(request, 'polizas.html', {'poliza': lista})

def nueva_poliza(request):
    lista_clientes = Cliente.objects.all()
    poliza = PolizaForm(request.POST or None)
    context = {
        'poliza':poliza,
        'cliente':lista_clientes,
    }
    if poliza.is_valid():
        poliza.save()
        return redirect('Clientes:polizas')
    return render(request, 'nueva_poliza.html', context)

def detallePolizas(request, id_poliza):
    polizas = Poliza.objects.get(pk=id_poliza)
    context = {
        'poliza':polizas
    }
    return render(request, 'poliza_detalle.html', context)

def editarPoliza(request, id_poliza):
    poliza = Poliza.objects.get(id=id_poliza)
    form = PolizaForm(request.POST or None, instance=poliza)
    if form.is_valid():
        form.save()
        return redirect('Clientes:polizas')
    return render(request, 'poliza_editar.html', {'form':form, 'poliza':poliza})

def eliminarPoliza(request, id_poliza):
    poliza = Poliza.objects.get(id = id_poliza)
    if request.method == 'POST':
        poliza.delete()
        return redirect('Clientes:polizas')
    return render(request,'poliza_eliminar.html', {'poliza':poliza})

def vistaPoliza(request, id_poliza):
    poliza = Poliza.objects.get(id = id_poliza)
    form = PolizaForm(request.POST or None, instance=poliza)
    return render(request,'poliza_vista.html', {'form':form,'poliza':poliza})

#Notificaciónes

def notificaciones(request):
    return render(request, 'notificaciones.html')