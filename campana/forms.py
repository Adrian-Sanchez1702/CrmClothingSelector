from django import forms
from .models import Campana

class CampanaForm(forms.ModelForm):

    class Meta:
        model = Campana
        fields = [
            'nombre',
            'publico_obj',
            'mensaje',
            'estado'
        ]