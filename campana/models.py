from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Campana(models.Model):
    id_cam = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    nombre = models.TextField()
    publico_obj = models.TextField()
    mensaje = models.TextField()
    estado = models.TextField()

    def __str__(self):
        return self.nombre

