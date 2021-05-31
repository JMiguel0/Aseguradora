from django import forms
from django.forms import fields, widgets 
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        
        
        model = Cliente
        fields = ['nombre', 'ap_paterno','ap_materno','fecha_nacimiento','email','num_celular','num_fijo','codigo_postal','colonia','direccion','rfc','fecha_registro','status']
        labels = {'nombre' : 'Nombre', 'ap_paterno':'Apellido Paterno','ap_materno':'Apellido Materno','fecha_nacimiento':'Fecha de Nacimiento','email':'Email','num_celular':'Número Móvil','num_fijo':'Número fijo','codigo_postal':'Código Postal','colonia':'Colonia','direccion':'Dirección','rfc':'R.F.C   ','fecha_registro':'Fecha de registro'}
        widgets = { 'nombre' : forms.TextInput(attrs={'class' : 'box'}),
                    'ap_paterno' : forms.TextInput(attrs={'class' : 'box'}),
                    'ap_materno' : forms.TextInput(attrs={'class' : 'box'}),
                    'fecha_nacimiento' : forms.DateInput(attrs={'class' : 'box' ,'type':'date'}),
                    'email' : forms.TextInput(attrs={'class' : 'box'}),
                    'num_celular' : forms.TextInput(attrs={'class' : 'box'}),
                    'num_fijo' : forms.TextInput(attrs={'class' : 'box'}),
                    'codigo_postal' : forms.TextInput(attrs={'class' : 'box'}),
                    'colonia' : forms.TextInput(attrs={'class' : 'box'}),
                    'direccion' : forms.TextInput(attrs={'class' : 'box'}),
                    'rfc' : forms.TextInput(attrs={'class' : 'box'}),
                    'fecha_registro' : forms.DateInput(attrs={'class' : 'box','type':'date'}),
                    'status' : forms.Select(attrs={'class' : 'box'} , choices=Status.objects.all()),
                    }

class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['num_poliza', 'deducible','fecha_inicio','fecha_termino','status','tipo_poliza','periodo_pago','cliente']
        labels = {'num_poliza': 'No. Póliza', 'deducible':'Deducible','fecha_inicio': 'Fecha inicio','fecha_termino':'Fecha término','status':'Status','tipo_poliza':'Tipo de Póliza','periodo_pago':'Perdiodo de Pago','cliente': 'Cliente'}
        widgets = { 'num_poliza' : forms.TextInput(attrs={'class' : 'box'}),
                    'deducible' : forms.TextInput(attrs={'class' : 'box'}),
                    'fecha_inicio' : forms.TextInput(attrs={'class' : 'box','type':'date'}),
                    'fecha_termino' : forms.DateInput(attrs={'class' : 'box' ,'type':'date'}),
                    'tipo_poliza' : forms.Select(attrs={'class' : 'box'} , choices=Tipos_Pago.objects.all()),
                    'periodo_pago' : forms.Select(attrs={'class' : 'box'} , choices=Periodos_Pago.objects.all()),
                    'cliente' : forms.Select(attrs={'class' : 'box'} , choices=Cliente.objects.all()),
                    'status' : forms.Select(attrs={'class' : 'box'} , choices=Status.objects.all()),
                    }
                   