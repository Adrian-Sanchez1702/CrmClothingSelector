from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Favorito
from catalogo.models import Catalogo
from datetime import date

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

    return redirect('lista_catalogo')  # regresa a tu lista

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