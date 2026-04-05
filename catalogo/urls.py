from django.urls import path
from .views import crear_catalogo, lista_catalogo, eliminar_producto, editar_producto

print("ANTES de importar views")

from . import views

print("DESPUÉS de importar views")

urlpatterns = [
    path("crear/", crear_catalogo, name="crear_catalogo"),
    path("lista/", lista_catalogo, name="lista_catalogo"),
    path("eliminar/<int:id>/", eliminar_producto, name="eliminar_producto"),
    path("editar/<int:id>/", editar_producto, name="editar_producto"),
]

print("URLPATTERNS DEFINIDO")