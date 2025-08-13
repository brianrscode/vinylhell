import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Articulo


@receiver(post_delete, sender=Articulo)
def eliminar_imagen_al_eliminar_articulo(sender, instance, **kwargs):
    if instance.ruta_foto:
        if os.path.isfile(instance.ruta_foto.path):
            os.remove(instance.ruta_foto.path)

@receiver(pre_save, sender=Articulo)
def eliminar_imagen_anterior_si_se_reemplaza(sender, instance, **kwargs):
    if not instance.pk:
        return  # El artículo es nuevo, no hay imagen anterior

    try:
        articulo_anterior = Articulo.objects.get(pk=instance.pk)
    except Articulo.DoesNotExist:
        return

    ruta_foto_anterior = articulo_anterior.ruta_foto
    nueva_ruta_foto = instance.ruta_foto

    if ruta_foto_anterior and ruta_foto_anterior != nueva_ruta_foto:
        if os.path.isfile(ruta_foto_anterior.path):
            os.remove(ruta_foto_anterior.path)
