from django.db import models
from django.contrib.auth.models import User
from campana.models import Campana  

class LeadCampana(models.Model):
    id_ledcam = models.AutoField(primary_key=True)

    campana = models.ForeignKey(
        Campana,
        on_delete=models.CASCADE
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    abrio_email = models.BooleanField(default=False)
    click = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} - {self.campana.nombre}"
