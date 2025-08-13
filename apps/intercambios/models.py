from django.db import models
from django.contrib.auth.models import User
from apps.articulos.models import Articulo
from apps.estados.models import EstadoIntercambio


# Pendiente, Aceptado, Cancelado
class Intercambio(models.Model):
    ofertante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="intercambios_ofertados")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="intercambios_recibidos", null=True, blank=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="intercambios")
    estado = models.ForeignKey(EstadoIntercambio, on_delete=models.PROTECT)
    lugar = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return f"Intercambio de {self.ofertante.username} por {self.articulo.nombre_articulo}"
