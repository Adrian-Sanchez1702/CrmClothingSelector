from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    
    ORIGEN_CHOICES = [
        ('redes', 'Redes'),
        ('tv', 'TV'),
        ('volantes', 'Volantes'),
        ('otro', 'Otro'),
    ]

    origen = forms.ChoiceField(choices=ORIGEN_CHOICES)

    class Meta:
        model = Lead
        fields = [
            "nombre", "ap", "am",
            "correo", "num_cel",
            "origen",
        ]