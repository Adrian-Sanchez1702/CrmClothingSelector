from django.urls import path
from .views import agregar_favorito, lista_favoritos, eliminar_favorito

urlpatterns = [
    path('favorito/<int:id>/', agregar_favorito, name='agregar_favorito'),
    path('', lista_favoritos, name='lista_favoritos'),
    path('eliminar/<int:id>/', eliminar_favorito, name='eliminar_favorito'),
]