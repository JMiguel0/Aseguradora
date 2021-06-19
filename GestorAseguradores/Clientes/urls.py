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
    path('polizas/editar/<int:id_poliza>',views.editarPoliza,name='editar_poliza'),
    path('polizas/eliminar/<int:id_poliza>',views.eliminarPoliza,name='eliminar_poliza'),
    path('polizas/<int:id_poliza>/vista',views.vistaPoliza,name='vista_poliza'),
    #Notificaciones
    path('notificaciones/',views.notificaciones,name='notificaciones'),
    #Primas
    path('polizas/<int:id_poliza>/nueva_prima',views.nueva_prima,name='nueva_prima'),
    path('polizas/primas/<int:id_prima>',views.detallePrima,name='detalle_prima'),
    path('polizas/<int:id_poliza>/editar/primas/<int:id_prima>',views.editarPrima,name='prima_editar'),
    path('polizas/<int:id_poliza>/eliminar/primas/<int:id_prima>',views.eliminarPrima,name='prima_eliminar'),
]
