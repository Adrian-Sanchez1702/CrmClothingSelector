from django.shortcuts import render
from favoritos.models import Favorito
from lead.models import Lead
from leadcampana.models import LeadCampana
from django.db.models import Count


def analisis(request):

    categoria_mas_visitada = Favorito.objects.values(
        'catalogo__categoria'
    ).annotate(total=Count('id_fav')).order_by('-total')

    fuentes_leads = Lead.objects.values(
        'origen'
    ).annotate(total=Count('id_lead')).order_by('-total')[:3]

    campanas_impacto = LeadCampana.objects.values(
        'campana__nombre'
    ).annotate(total_clicks=Count('click')).order_by('-total_clicks')

    contexto = {
        'categoria': categoria_mas_visitada,
        'fuentes': fuentes_leads,
        'campanas': campanas_impacto
    }

    return render(request, 'analisis/analisis.html', contexto)