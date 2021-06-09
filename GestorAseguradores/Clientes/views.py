

from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import ClienteForm, PolizaForm

# Clientes
def index(request):
    
    lista_clientes = Cliente.objects.filter(agente=request.user)
    print("Holaaaa",lista_clientes)
    print(type(lista_clientes))
    return render(request, 'clientes.html', {'lista': lista_clientes})

def nuevo(request):
    cliente = ClienteForm(request.POST or None)
    status = Status.objects.all()
    if cliente.is_valid():
        instance = cliente.save(commit=False)
        instance.agente = request.user
        instance.save()
        return redirect('Clientes:index')
    return render(request, 'registro_cliente.html', {'cliente': cliente, 'status':status})

def detalle(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    context = {
        'cliente':cliente
    }
    return render(request, 'detalle.html', context)

#Pólizas 

def polizas(request):

    lista_polizas = Poliza.objects.none()
    cliente = Cliente.objects.filter(agente = request.user)
    for usuario in cliente:
        lista_polizas  |= Poliza.objects.filter(cliente = usuario)

    print(type(lista_polizas))
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

#Notificaciónes

def detallePolizas(request, id_cliente, id_poliza):
    polizas = Poliza.objects.get(pk=id_poliza)
    context = {
        'poliza':polizas
    }
    return render(request, 'detalle.html', context)