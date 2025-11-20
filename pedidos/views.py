from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import Pedido, LineaPedido
from tienda.models import Producto  # Import Producto to fetch instances
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url="autenticacion/login")
def procesar(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas = []

    for key, value in carro.carro.items():
        producto = Producto.objects.get(id=key)  # Fetch the Producto instance
        lineas.append(LineaPedido(
            producto=producto,  # Use the instance, not just the ID
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
            precio=producto.precio  # Assuming Producto has a precio field
        ))

    LineaPedido.objects.bulk_create(lineas)

    enviar_mail(
        pedido=pedido,
        lineas=lineas,
        nombre_usuario=request.user.username,  # Consistent naming
        email_usuario=request.user.email
    )

    messages.success(request, "El pedido se ha creado correctamente")
    return redirect("../tienda")

# En pedidos/views.py
def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("email/pedidos.html", {
        "pedido": kwargs.get("pedido"),
        "lineas": kwargs.get("lineas"),
        "nombre_usuario": kwargs.get("nombre_usuario"),
    })
    mensaje_txt = strip_tags(mensaje)
    from_email = "betower25@gmail.com"
    to = kwargs.get("email_usuario")
    
    print(f"Intentando enviar correo a: {to}")  # ¿A quién va?
    if not to:
        print("¡Jajja, no hay email! ¿A dónde lo mando? 😂")
        return

    try:
        send_mail(asunto, mensaje_txt, from_email, [to], html_message=mensaje, fail_silently=False)
        print("¡Correo enviado! ¡Éxito total, jajja! 🎉")
    except Exception as e:
        print(f"¡Oops, falló! Error: {e} 😅")