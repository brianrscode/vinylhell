from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import EstadoArticulo, EstadoIntercambio


@receiver(post_migrate)
def create_initial_states(sender, **kwargs):
    estados = ['Disponible', 'Intercambiado']
    for estado in estados:
        EstadoArticulo.objects.get_or_create(nombre=estado)


@receiver(post_migrate)
def create_initial_states(sender, **kwargs):
    estados = ['Pendiente', 'Aceptado', 'Rechazado']
    for estado in estados:
        EstadoIntercambio.objects.get_or_create(nombre=estado)
