from django.urls import path
from .views import form_del_producto, form_mod_producto, home , mostrar, form_producto, form_mod_producto

urlpatterns = [
    path('',home,name="home"),
    path('mostrar',mostrar,name="mostrar"),
    path('agregar_producto',form_producto,name='form_producto'),
    path('modificar_producto/<id>',form_mod_producto,name='form_mod_producto'),
    path('borrar_producto/<id>',form_del_producto,name='form_del_producto')
]
