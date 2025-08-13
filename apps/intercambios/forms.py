from django import forms
from .models import Intercambio


class IntercambioForm(forms.ModelForm):
    class Meta:
        model = Intercambio
        # Solo pedimos lugar y fecha porque el ofertante, el artículo y el estado inicial los pondremos en la vista.
        fields = ['lugar', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }


class IntercambioForm(forms.ModelForm):
    class Meta:
        model = Intercambio
        fields = ['lugar', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        self.articulo = kwargs.pop('articulo', None)  # Pasaremos el artículo desde la vista
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        # Validar que haya artículo
        if not self.articulo:
            raise forms.ValidationError("No se ha especificado un artículo.")

        # Validar estado del artículo
        if self.articulo.estado == "Intercambiado":
            raise forms.ValidationError("Este artículo ya no está disponible para intercambio.")

        # Validar que no sea del mismo usuario
        if self.articulo.usuario == self.request.user:
            raise forms.ValidationError("No puedes solicitar un intercambio de tu propio artículo.")

        return cleaned_data