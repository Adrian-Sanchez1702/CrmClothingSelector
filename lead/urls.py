from django.urls import path
from .views import crear_lead, lista_leads, eliminar_lead

urlpatterns = [
    path("nuevo/", crear_lead, name="crear_lead"),
    path("lista/", lista_leads, name="lista_leads"),
    path("eliminar/<int:id_lead>/", eliminar_lead, name="eliminar_lead"),
]