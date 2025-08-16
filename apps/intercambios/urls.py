from django.urls import path
from .views import (
    solicitar_intercambio,
    mis_solicitudes,
    cambiar_estado_intercambio,
    cancelar_solicitud,
)

urlpatterns = [
    path('solicitar/<int:articulo_id>/', solicitar_intercambio, name='solicitar_intercambio'),
    path('mis_solicitudes/', mis_solicitudes, name='mis_solicitudes'),
    path('cambiar_estado/<int:intercambio_id>/<str:nuevo_estado>/', cambiar_estado_intercambio, name='cambiar_estado_intercambio'),
    path('cancelar_solicitud/', cancelar_solicitud, name='cancelar_solicitud'),
]
