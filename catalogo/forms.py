from django import forms
from .models import Catalogo

class CatalogoForm(forms.ModelForm):

    class Meta:
        model = Catalogo
        fields = [
            "nombre",
            "categoria",
            "tipo_prenda",
            "descripcion",
            "img"
        ]