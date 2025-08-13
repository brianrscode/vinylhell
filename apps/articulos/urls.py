from django.urls import path
from .views import (
    index,
    detalle_articulo,
    agregar_articulo,
    editar_articulo,
    eliminar_articulo
)


urlpatterns = [
    path('', index, name='index'),
    path('detalle_articulo/<int:articulo_id>/', detalle_articulo, name='detalle_articulo'),
    path('agregar_articulo/', agregar_articulo, name='agregar_articulo'),
    path('editar_articulo/<int:articulo_id>/', editar_articulo, name='editar_articulo'),
    path('eliminar_articulo/<int:articulo_id>/', eliminar_articulo, name='eliminar_articulo'),
]
