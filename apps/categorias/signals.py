from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Categoria


@receiver(post_migrate)
def create_initial_states(sender, **kwargs):
    # Categorías de artículos de metal y rock
    categorias = ["Disco", "Vinilo", "Parche", "Ropa", "Cinturón", "Gafas", "Instrumento", "Otros"]
    for categoria in categorias:
        Categoria.objects.get_or_create(nombre=categoria)