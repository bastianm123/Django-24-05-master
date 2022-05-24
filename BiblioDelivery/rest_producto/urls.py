from django.urls import path
from rest_producto.views import lista_productos, detalle_producto

urlpatterns = [
    path('lista_productos',lista_productos,name="lista_productos"),
    path('buscar_producto/<id>',detalle_producto,name='buscar_producto')
]
