# se crean las funciones para cada necesidad que vamos a tener

def agregar_producto(inventario, nombre, precio, cantidad):
    """""
    Agrega un producto al inventario.
        inventario (list): lista de productos
        nombre (str): nombre del producto
        precio (float): precio del producto
        cantidad (int): cantidad disponible
    """
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)


def mostrar_inventario(inventario):
    
    #Muestra todos los productos del inventario.
    
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- Inventario ---")
    for p in inventario:
        print(f"Producto: {p['nombre']} | Precio: {p['precio']:.3f} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.
    Retorna el producto o None.
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas básicas.
    Retorna un diccionario con los resultados.
    """
    if not inventario:
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }

