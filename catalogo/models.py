from django.db import models
from django.contrib.auth.models import User

class Catalogo(models.Model):

    CATEGORIAS = [
        ("hombre", "Hombre"),
        ("mujer", "Mujer"),
        ("niño", "Niño"),
    ]

    TIPOS = [
        ("playera", "Playera"),
        ("pantalon", "Pantalón"),
        ("sudadera", "Sudadera"),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    tipo_prenda = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField()
    img = models.ImageField(upload_to="catalogo/", null=True, blank=True)

    def __str__(self):
        return self.nombre

