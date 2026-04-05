from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Favorito
from catalogo.models import Catalogo
from lead.models import Lead
from datetime import date
from collections import Counter

@login_required
def agregar_favorito(request, id):
    catalogo = Catalogo.objects.get(id=id)

    # evitar duplicados
    if not Favorito.objects.filter(usuario=request.user, catalogo=catalogo).exists():
        Favorito.objects.create(
            usuario=request.user,
            catalogo=catalogo,
            fecha=date.today()
        )

    #  OBTENER LEAD DEL USUARIO
    lead = Lead.objects.get(usuario=request.user)

    #  OBTENER TODOS SUS FAVORITOS
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('catalogo')

    #  CONTAR CATEGORÍAS
    categorias = [f.catalogo.categoria for f in favoritos]

    if categorias:
        conteo = Counter(categorias)
        categoria_mas_comun = conteo.most_common(1)[0][0]

        #  ASIGNAR CATEGORIA FAVORITA
        lead.categoria_fav = categoria_mas_comun

    #  CAMBIAR TIPO DE LEAD
    if favoritos.count() >= 10:
        lead.tipo_lead = 'recurrente'

    # guardar cambios
    lead.save()

    return redirect('lista_catalogo')

@login_required
def lista_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('catalogo')
    return render(request, 'favoritos/lista_favoritos.html', {
        'favoritos': favoritos
    })

def eliminar_favorito(request, id):
    fav = get_object_or_404(Favorito, id_fav=id, usuario=request.user)
    fav.delete()
    return redirect('lista_favoritos')