from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre_articulo', 'descripcion', 'bien_esperado', 'ruta_foto', 'categoria', 'estado']