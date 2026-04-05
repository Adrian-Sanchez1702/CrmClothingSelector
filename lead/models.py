from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):

    TIPOS_LEAD = [
        ('nuevo', 'Nuevo'),
        ('recurrente', 'Recurrente'),
        ('inactivo', 'Inactivo'),
    ]

    id_lead = models.AutoField(primary_key=True)

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    nombre = models.TextField()
    ap = models.TextField()
    am = models.TextField()
    num_cel = models.TextField()
    correo = models.TextField()
    origen = models.TextField()

    tipo_lead = models.CharField(
        max_length=20,
        choices=TIPOS_LEAD,
        default='nuevo'
    )

    categoria_fav = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre