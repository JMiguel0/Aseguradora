from django.contrib.auth.models import User
from .models import Agente
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Agente, UserAdmin)



