

from django.db import close_old_connections
from django.db.models import query
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from django.contrib import messages

# Clientes
def index(request):
    queryset = request.GET.get("buscar")
    if queryset:
        lista_cliente = Cliente.objects.filter((Q(nombre__icontains=queryset) | Q(ap_paterno__icontains=queryset) | Q(ap_materno__icontains=queryset)| Q(num_celular__icontains=queryset) )& Q(agente=request.user))

        return render(request, 'clientes.html', {'lista': lista_cliente})
    else:
        lista_clientes = Cliente.objects.filter(agente=request.user)
        return render(request, 'clientes.html', {'lista': lista_clientes})

    #lista_clientes = Cliente.objects.filter(agente=request.user)
    #return render(request, 'clientes.html', {'lista': lista_clientes})

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
    queryset = request.GET.get("buscar")
    if queryset:
        lista_polizas = Poliza.objects.none()
        cliente = Cliente.objects.filter(agente = request.user)
        for usuario in cliente:
            lista_polizas  |= Poliza.objects.filter(Q(cliente = usuario) & Q(num_poliza__icontains=queryset))
        lista = list(lista_polizas)
        return render(request, 'polizas.html', {'poliza': lista})
    else:
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
    primas = Prima.objects.filter(poliza_id = id_poliza)
    context = {
        'poliza':polizas,
        'primas':primas
    }
    return render(request, 'poliza_detalle.html', context)

def editarPoliza(request, id_poliza):
    poliza = Poliza.objects.get(id=id_poliza)
    form = PolizaForm(request.POST or None, instance=poliza)
    if form.is_valid():
        form.save()
        return redirect('Clientes:detalle_poliza', id_poliza)
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

#Primas

def nueva_prima(request, id_poliza):
    form = PrimaForm(request.POST or None)
    context = {
     'form':form 
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        poliza1 = Poliza.objects.get(id = id_poliza)
        instance.comision_agente = "16"
        instance.poliza = poliza1
        instance.save()
        return redirect('Clientes:detalle_poliza', id_poliza)
    return render(request, 'nueva_prima.html', context)

def detallePrima(request, id_prima):
    
    prima = Prima.objects.get(id = id_prima)
    form = PrimaForm(request.POST or None, instance=prima)
    context = {
        'form':form,
    }
    return render(request, 'vista_prima.html', context)

def editarPrima(request, id_poliza, id_prima):
    prima = Prima.objects.get(id=id_prima)
    form = PrimaForm(request.POST or None, instance=prima)
    context = {
     'form':form,
     'prima':prima
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        poliza1 = Poliza.objects.get(id = id_poliza)
        instance.comision_agente = "16"
        instance.poliza = poliza1
        instance.save()
        return redirect('Clientes:detalle_poliza', id_poliza)
    return render(request, 'prima_editar.html', context)

def eliminarPrima(request, id_poliza, id_prima):
    prima = Prima.objects.get(id = id_prima)
    if request.method == 'POST':
        prima.delete()
        return redirect('Clientes:detalle_poliza', id_poliza)
    return render(request,'prima_eliminar.html', {'prima':prima})

    #Notificaciónes

def notificaciones(request):
    queryset = request.GET.get("buscar")
    if queryset:
        lista_polizas = Poliza.objects.none()
        lista_primas = Prima.objects.none()
        cliente = Cliente.objects.filter(agente = request.user)
        
        for usuario in cliente:
            lista_polizas  |= Poliza.objects.filter(cliente = usuario)
        lista = list(lista_polizas)
        for prima in lista:
            lista_primas |= Prima.objects.filter(Q(poliza = prima, status = 1) & Q(no_prima__icontains = queryset) )
        lista_primas_agente = list(lista_primas)
        return render(request, 'notificaciones.html',{'primas': lista_primas_agente})
    else:
        lista_polizas = Poliza.objects.none()
        lista_primas = Prima.objects.none()
        cliente = Cliente.objects.filter(agente = request.user)
        
        for usuario in cliente:
            lista_polizas  |= Poliza.objects.filter(cliente = usuario)
        lista = list(lista_polizas)
        for prima in lista:
            lista_primas |= Prima.objects.filter(poliza = prima, status = 1)
        lista_primas_agente = list(lista_primas)
        return render(request, 'notificaciones.html',{'primas': lista_primas_agente})

def notificaciones_estado(request, id_prima):
    prima = Prima.objects.get(id=id_prima)
    form = PrimaForm(request.POST or None, instance=prima)
    instance = form.save(commit=False)
    instance.status = Status.objects.get(id = 2)
    instance.save()
    
    lista_polizas = Poliza.objects.none()
    lista_primas = Prima.objects.none()
    cliente = Cliente.objects.filter(agente = request.user)
    
    for usuario in cliente:
        lista_polizas  |= Poliza.objects.filter(cliente = usuario)
    lista = list(lista_polizas)
    for prima in lista:
        lista_primas |= Prima.objects.filter(poliza = prima, status = 1)
    lista_primas_agente = list(lista_primas)
    return render(request, 'notificaciones.html',{'primas': lista_primas_agente})
    
def enviar_notificacion(request, id_prima):
    #Encontrar al cliente de la prima
    prima1 = Prima.objects.get(id = id_prima)
    poliza1 = Poliza.objects.get(id = prima1.poliza.id)
    cliente1 = Cliente.objects.get(id = poliza1.cliente.id)
    
    #Enviar email
    asunto = "Recuerde pagar su póliza de seguro número " + str(prima1.poliza)
    mensaje = "Hola {} {}. Este correo es para recordarle el pago de la prima número {} de la póliza {}, favor de pagar MXN{} antes del {}. Gracias. ".format( str(cliente1.nombre), str(cliente1.ap_paterno),str(prima1.no_prima), str(prima1.poliza),str(prima1.total_pagar),str(prima1.fecha_vencimiento))
    email = EmailMessage(asunto, mensaje, 'archiherr@gmail.com',[cliente1.email])
    email.send()
    messages.success(request,'Email enviado exitosamente a '+str(cliente1.email))
    
    
    return redirect('Clientes:notificaciones')
def estadisticas(request):

    lista_polizas = Poliza.objects.none()
    lista_primas = Prima.objects.none()
    cliente = Cliente.objects.filter(agente = request.user)
    
    for usuario in cliente:
        lista_polizas  |= Poliza.objects.filter(cliente = usuario)
    lista = list(lista_polizas)
    for prima in lista:
        lista_primas |= Prima.objects.filter(poliza = prima, status = 2)
    lista_primas_agente = list(lista_primas)

    cantidad_mensual = 0.0
    
    data = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    for prima in lista_primas_agente:
        casilla = asignar_fecha(str(prima.fecha_vencimiento))
        casilla = int(casilla)
        casilla = casilla-1
        cantidad_mensual = data[casilla] + (float(prima.total_pagar))*((float(prima.comision_agente)/100))
        data[casilla] = cantidad_mensual
        cantidad_mensual = 0.0

    labels = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    
    return render(request, 'estadisticas.html', {'labels':labels, 'data':data})

def asignar_fecha(num):
    num = num[5:7]
    mes = ""
    if(num == "01"):
        mes = "Enero"
    if(num== ("02")):
        mes = "Febrero"
    if(num== ("03")):
        mes = "Marzo"
    if(num== ("04")):
        mes = "Abril"
    if(num== ("05")):
        mes = "Mayo"
    if(num== ("06")):
        mes = "Junio"
    if(num== ("07")):
        mes = "Julio"
    if(num== ("08")):
        mes = "Agosto"
    if(num== ("09")):
        mes = "Septiembre"
    if(num== ("10")):
        mes = "Octubre"
    if(num== ("11")):
        mes = "Noviembre"
    if(num== ("12")):
        mes = "Diciembre"   
    if(num.startswith("0")):
        num = num[1]
    return num
    
    
    