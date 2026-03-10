from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("lista_leads")  # luego se hace esta vista catalogo
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "accounts/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ese usuario ya existe")
            return redirect("crear_lead")

        user = User.objects.create_user(
            username=username,
            password=password
        )

        #asignar grupo "cliente"
        group, created = Group.objects.get_or_create(name="cliente")
        user.groups.add(group)

        messages.success(request, "Usuario creado correctamente")
        return redirect("crear_lead")