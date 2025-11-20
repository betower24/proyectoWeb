class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            self.carro = self.session["carro"] = {}
        else:
            self.carro = carro

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            try:
                self.carro[producto_id] = {
                    "producto_id": producto.id,
                    "nombre": producto.nombre,
                    "precio": str(producto.precio),  # Mantengo como string por tu diseño
                    "cantidad": 1,
                    "imagen": producto.imagen.url if producto.imagen else ""
                }
            except AttributeError as e:
                # Manejo de error si producto no tiene los atributos esperados
                print(f"Error al agregar producto: {e}")
                return
        else:
            self.carro[producto_id]["cantidad"] += 1
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()

    def restar_producto(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            if self.carro[producto_id]["cantidad"] > 1:
                self.carro[producto_id]["cantidad"] -= 1
            else:
                self.eliminar(producto)
            self.guardar_carro()

    def limpiar(self):
        self.session["carro"] = {}
        self.session.modified = True