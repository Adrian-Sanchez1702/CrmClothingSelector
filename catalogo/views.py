from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import CatalogoForm
from .models import Catalogo


def crear_catalogo(request):

    if request.method == "POST":
        form = CatalogoForm(request.POST, request.FILES)

        if form.is_valid():
            catalogo = form.save(commit=False)
            catalogo.usuario = request.user
            catalogo.save()

            return redirect("lista_catalogo")

    else:
        form = CatalogoForm()

    return render(request, "catalogo/agregar_catalogo.html", {
        "form": form
    })


def lista_catalogo(request):

    productos = Catalogo.objects.all()

    search = request.GET.get("search")

    if search:
        productos = productos.filter(
            Q(nombre__icontains=search) |
            Q(descripcion__icontains=search)
        )

    categoria = request.GET.get("categoria")
    tipo = request.GET.get("tipo_prenda")

    if categoria:
        productos = productos.filter(categoria=categoria)

    if tipo:
        productos = productos.filter(tipo_prenda=tipo)

    return render(request, "catalogo/lista_catalogo.html", {
        "productos": productos
    })


def eliminar_producto(request, id):

    producto = get_object_or_404(Catalogo, id=id)
    producto.delete()

    return redirect("lista_catalogo")


def editar_producto(request, id):

    producto = get_object_or_404(Catalogo, id=id)

    if request.method == "POST":

        form = CatalogoForm(request.POST, request.FILES, instance=producto)

        if form.is_valid():
            form.save()
            return redirect("lista_catalogo")

    else:
        form = CatalogoForm(instance=producto)

    return render(request, "catalogo/editar_catalogo.html", {
        "form": form
    })
