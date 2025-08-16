from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import IntercambioForm
from apps.articulos.models import Articulo
from apps.estados.models import EstadoIntercambio
from apps.estados.models import EstadoArticulo
from .models import Intercambio


@login_required
def solicitar_intercambio(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    # Evitar que el dueño del artículo se ofrezca a sí mismo
    if articulo.propietario == request.user:
        return redirect('detalle_articulo', articulo_id=articulo.id)

    if request.method == 'POST':
        form = IntercambioForm(request.POST)
        if form.is_valid():
            intercambio = form.save(commit=False)
            intercambio.ofertante = request.user
            intercambio.receptor = articulo.propietario
            intercambio.articulo = articulo
            intercambio.estado = EstadoIntercambio.objects.get(nombre="Pendiente")
            intercambio.save()
            # return redirect('detalle_articulo', articulo_id=articulo.id)
            # Redireccionar al inicio y mandar un mensaje de éxito
            messages.success(request, "Solicitud de intercambio enviada con éxito.")
            return redirect('index')
    else:
        form = IntercambioForm()

    return render(request, 'intercambios/solicitar_intercambio.html', {
        'form': form,
        'articulo': articulo
    })

@login_required
def mis_solicitudes(request):
    enviadas = Intercambio.objects.filter(ofertante=request.user)
    recibidas = Intercambio.objects.filter(receptor=request.user)

    return render(request, 'intercambios/mis_solicitudes.html', {
        'enviadas': enviadas,
        'recibidas': recibidas
    })


@login_required
def cambiar_estado_intercambio(request, intercambio_id, nuevo_estado):
    intercambio = get_object_or_404(Intercambio, id=intercambio_id, receptor=request.user)

    try:
        estado = EstadoIntercambio.objects.get(nombre=nuevo_estado)
    except EstadoIntercambio.DoesNotExist:
        messages.error(request, "Estado inválido.")
        return redirect('mis_solicitudes')

    intercambio.estado = estado
    intercambio.save()

    # Si se acepta, cambiar estado del artículo y rechazar otros intercambios pendientes
    if nuevo_estado.lower() == "aceptado":
        try:
            estado_intercambiado = EstadoArticulo.objects.get(nombre="Intercambiado")
        except EstadoArticulo.DoesNotExist:
            messages.error(request, "El estado 'Intercambiado' no existe en EstadoArticulo.")
            return redirect('mis_solicitudes')

        # Cambiar estado del artículo
        articulo = intercambio.articulo
        articulo.estado = estado_intercambiado
        articulo.save()

        # Rechazar otros intercambios pendientes de este artículo
        try:
            estado_rechazado = EstadoIntercambio.objects.get(nombre="Rechazado")
            estado_pendiente = EstadoIntercambio.objects.get(nombre="Pendiente")
        except EstadoIntercambio.DoesNotExist:
            messages.error(request, "Estados 'Pendiente' o 'Rechazado' no existen en EstadoIntercambio.")
            return redirect('mis_solicitudes')

        Intercambio.objects.filter(
            articulo=articulo,
            estado=estado_pendiente
        ).exclude(id=intercambio.id).update(estado=estado_rechazado)

    messages.success(request, f"Intercambio {nuevo_estado.lower()} con éxito.")
    return redirect('mis_solicitudes')


@login_required
def cancelar_solicitud(request):
    if request.method == 'POST':
        articulo_id = request.POST.get('articulo_id')
        try:
            # Buscar y eliminar la solicitud de intercambio
            # Busca el Intercambio que tenga el artículo que se está solicitando
            # relacionado con el usuario autenticado
            # y que esté en estado pendiente
            intercambio = Intercambio.objects.get(
                ofertante=request.user,
                articulo_id=articulo_id,
                estado__nombre="Pendiente"
            )
            intercambio.delete()
            messages.success(request, "Solicitud de intercambio cancelada correctamente.")
        except Intercambio.DoesNotExist:
            messages.error(request, "No se encontró la solicitud de intercambio o no se puede cancelar.")

    return redirect('detalle_articulo', articulo_id=articulo_id)
