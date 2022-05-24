from django.contrib import admin
from .models import Producto,Cliente,Categoria

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Categoria)