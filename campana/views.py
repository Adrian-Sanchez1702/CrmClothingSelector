from django.shortcuts import render, redirect, get_object_or_404
from .forms import CampanaForm
from .models import Campana

def agregar_campana(request):

    if request.method == 'POST':
        form = CampanaForm(request.POST)

        if form.is_valid():
            campana = form.save(commit=False)
            campana.usuario = request.user
            campana.save()

            return redirect('listar_campanas')

    else:
        form = CampanaForm()

    return render(request, 'campana/agregar_campana.html', {'form': form})



def listar_campanas(request):
    campanas = Campana.objects.all()

    return render(request, 'campana/listar_campanas.html', {
        'campanas': campanas
    })


def eliminar_campana(request, id):
    campana = get_object_or_404(Campana, id_cam=id)
    campana.delete()
    return redirect('listar_campanas')

def editar_campana(request, id):

    campana = get_object_or_404(Campana, id_cam=id)

    if request.method == "POST":

        campana.nombre = request.POST.get('nombre')
        campana.publico_obj = request.POST.get('publico_obj')
        campana.mensaje = request.POST.get('mensaje')
        campana.estado = request.POST.get('estado')

        campana.save()

        return redirect('listar_campanas')

    return render(request, 'campana/editar_campana.html', {
        'campana': campana
    })