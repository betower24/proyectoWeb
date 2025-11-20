from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from django.contrib import messages

class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            auth_login(request, usuario)  # Usamos auth_login en lugar de login
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, "registro/registro.html", {"form": form})

def cerra_sesion(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('home')

def login_view(request):  # Renombrado de login a login_view
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            auth_login(request, usuario)  # Usamos auth_login en lugar de login
            messages.success(request, "Has iniciado sesión exitosamente.")
            return redirect('home')
        else:
            messages.error(request, "Credenciales inválidas. Intenta de nuevo.")
    else:
        form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})