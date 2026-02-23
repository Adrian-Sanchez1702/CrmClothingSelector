from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Catalogo  

class Favorito(models.Model):
    id_fav = models.AutoField(primary_key=True)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    catalogo = models.ForeignKey(
        Catalogo,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()

    def __str__(self):
        return f"{self.usuario.username} - {self.catalogo.nombre}"