from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Articulo
from .forms import ArticuloForm


def index(request):
    articulos = Articulo.objects.filter(estado__nombre="Disponible").order_by('-fecha_publicacion')
    return render(request, 'index.html', {'articulos': articulos})


def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo})


@login_required
def agregar_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.propietario = request.user
            articulo.save()
            return redirect('index')
    else:
        form = ArticuloForm()
    return render(request, 'articulos/agregar_articulo.html', {'form': form})


@login_required
def editar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if articulo.propietario != request.user:
        return HttpResponseForbidden("No tienes permiso para editar este artículo.")

    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('detalle_articulo', articulo_id=articulo.id)
    else:
        form = ArticuloForm(instance=articulo)

    return render(request, 'articulos/editar_articulo.html', {'form': form})


@login_required
def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)

    if articulo.propietario != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este artículo.")

    if request.method == "POST":
        articulo.delete()
        return redirect('index')

    return render(request, 'articulos/confirmar_eliminar.html', {'articulo': articulo})