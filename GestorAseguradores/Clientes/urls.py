from django.urls.resolvers import URLPattern

from . import views
from django.urls import path

app_name = 'Clientes'
urlpatterns = [
    #/Clientes/
    path('',views.index,name='index'),
    path('nuevo',views.nuevo,name='nuevo'),
    path('<int:id_cliente>/',views.detalle,name='detalle'),
    path('editar/<int:id_cliente>/',views.editar,name='editar'),
    path('eliminar/<int:id_cliente>/',views.eliminar,name='eliminar'),
    #Pólizas
    path('polizas/',views.polizas,name='polizas'),
    path('nueva_poliza/',views.nueva_poliza,name='nueva_poliza'),
    path('polizas/<int:id_poliza>',views.detallePolizas,name='detalle_poliza'),
    #Notificaciones
    path('notificaciones/',views.notificaciones,name='notificaciones'),


]
