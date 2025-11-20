from django.shortcuts import render, redirect
from .forms import Formulario
from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto = Formulario()

    if request.method == "POST":
        formulario_contacto = Formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            email = EmailMessage(
                "mensaje desde django",
                "el usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido),
                "",
                ["betower25@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # Aquí podrías agregar lógica, como guardar en la base de datos o enviar un email
                return redirect("/contacto/?valido")
            except:
                # Si ocurre un error al enviar el correo, puedes manejarlo aquí
                return redirect("/contacto/?error")

    return render(request, "contacto/contacto.html", {'miformulario': formulario_contacto})
