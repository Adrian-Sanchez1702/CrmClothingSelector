from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import LeadForm
from .models import Lead

def crear_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.usuario = request.user
            lead.save()
            return redirect("lista_leads")
    else:
        form = LeadForm()

    return render(request, "leads/agregar_lead.html", {"form": form})

def lista_leads(request):
    leads = Lead.objects.all()

    # buscador
    search = request.GET.get("search")
    if search:
        leads = leads.filter(
            Q(nombre__icontains=search) |
            Q(ap__icontains=search) |
            Q(am__icontains=search) |
            Q(correo__icontains=search) |
            Q(num_cel__icontains=search)
        )

    
    categoria = request.GET.get("categoria_fav")
    tipo = request.GET.get("tipo_lead")
    origen = request.GET.get("origen")

    if categoria:
        leads = leads.filter(categoria_fav=categoria)

    if tipo:
        leads = leads.filter(tipo_lead=tipo)

    if origen:
        leads = leads.filter(origen=origen)

    return render(request, "leads/lista_leads.html", {"leads": leads})


def eliminar_lead(request, id_lead):
    lead = get_object_or_404(Lead, id_lead=id_lead)
    lead.delete()
    return redirect("lista_leads")


def editar_lead(request, id_lead):
    lead = get_object_or_404(Lead, id_lead=id_lead, usuario=request.user)

    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("lista_leads")
    else:
        form = LeadForm(instance=lead)

    return render(request, "leads/editar_lead.html", {
        "form": form,
        "lead": lead
    })