from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_campana, name='agregar_campana'),       
    path('campanas/', views.listar_campanas, name='listar_campanas'),
    path('eliminar_campana/<int:id>/', views.eliminar_campana, name='eliminar_campana'),
    path('editar/<int:id>/', views.editar_campana, name='editar_campana'),
]