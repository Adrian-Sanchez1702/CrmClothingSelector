from django.db import models
from django.contrib.auth.models import User

class Catalogo(models.Model):
    id_cat = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    nombre = models.TextField()
    descripcion = models.TextField()
    categoria = models.TextField()
    tipo_prenda = models.TextField()
    img = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

