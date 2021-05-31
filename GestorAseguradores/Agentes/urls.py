from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

app_name = 'Agentes'
urlpatterns = [
    path('',views.index,name='index'),
]