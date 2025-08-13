from django.urls import path
from .views import (
    solicitar_intercambio,
    mis_solicitudes,
    cambiar_estado_intercambio,
    # intercambios_recibidos,
    # intercambios_enviados
)

urlpatterns = [
    path('solicitar/<int:articulo_id>/', solicitar_intercambio, name='solicitar_intercambio'),
    path('mis_solicitudes/', mis_solicitudes, name='mis_solicitudes'),
    path('cambiar_estado/<int:intercambio_id>/<str:nuevo_estado>/', cambiar_estado_intercambio, name='cambiar_estado_intercambio'),

    # path('intercambios_recibidos/', intercambios_recibidos, name='intercambios_recibidos'),
    # path('intercambios_enviados/', intercambios_enviados, name='intercambios_enviados'),
]
