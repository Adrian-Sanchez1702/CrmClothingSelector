from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Campana
from leadcampana.services import enviar_campana

@receiver(post_save, sender=Campana)
def enviar_correo_automatico(sender, instance, created, **kwargs):

    if created and instance.estado == "Activa":
        enviar_campana(instance)