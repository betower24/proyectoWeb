def importe_total_carro(request):
    total = 0
    try:
        if "carro" in request.session:
            for key, value in request.session["carro"].items():
                precio = float(value["precio"])  # Convertir a float
                cantidad = value.get("cantidad", 1)  # Por si falta cantidad
                total += precio * cantidad
    except (ValueError, KeyError) as e:
        print(f"Error al calcular total: {e}")
    return {"importe_total_carro": total}  