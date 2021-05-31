

from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import ClienteForm, PolizaForm

# Clientes
def index(request):
    
    lista_clientes = Cliente.objects.filter(agente=request.user)
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
    
    lista_polizas = Poliza.objects.all()
    return render(request, 'polizas.html', {'poliza': lista_polizas})

def nueva_poliza(request):
    lista_clientes = Cliente.objects.all()
    poliza = PolizaForm(request.POST or None)
    context = {
        'poliza':poliza,
        'cliente':lista_clientes,
    }
    print("siuuuuu", request)
    print("siuuuuuaa", request.POST)
    if poliza.is_valid():
        poliza.save()
        return redirect('Clientes:polizas')
    return render(request, 'nueva_poliza.html', context)

#Notificaciónes
