from django.db import models
from django.contrib.auth.models import User
from apps.categorias.models import Categoria
from apps.estados.models import EstadoArticulo



class Articulo(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articulos")
    nombre_articulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    bien_esperado = models.CharField(max_length=50)
    ruta_foto = models.ImageField(upload_to="articulos/")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    estado = models.ForeignKey(EstadoArticulo, on_delete=models.PROTECT)
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_articulo} ({self.propietario.username})"
