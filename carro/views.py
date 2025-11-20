from django.shortcuts import render, redirect
from .carro import Carro  # Cambiado a mayúscula
from tienda.models import Producto
from django.http import Http404

def tienda(request):
    try:
        productos = Producto.objects.all()
        carro = Carro(request)  # Instancia correcta
        print("Carrito en sesión:", request.session.get("carro", {}))  # Debug
        return render(request, "tienda/tienda.html", {"productos": productos, "carro": carro})
    except Exception as e:
        print(f"Error en vista tienda: {e}")
        return render(request, "tienda/tienda.html", {"productos": [], "carro": None})

def agregar_prod(request, producto_id):
    carro = Carro(request)
    try:
        producto = Producto.objects.get(id=producto_id)
        carro.agregar(producto=producto)
    except Producto.DoesNotExist:
        raise Http404("Producto no encontrado")
    except Exception as e:
        print(f"Error al agregar producto: {e}")
    return redirect("tienda")

def eliminar_prod(request, producto_id):
    carro = Carro(request)
    try:
        producto = Producto.objects.get(id=producto_id)
        carro.eliminar(producto=producto)
    except Producto.DoesNotExist:
        raise Http404("Producto no encontrado")
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
    return redirect("tienda")

def restar_prod(request, producto_id):
    carro = Carro(request)
    try:
        producto = Producto.objects.get(id=producto_id)
        carro.restar_producto(producto=producto)
    except Producto.DoesNotExist:
        raise Http404("Producto no encontrado")
    except Exception as e:
        print(f"Error al restar producto: {e}")
    return redirect("tienda")

def limpiar_car(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect("tienda")