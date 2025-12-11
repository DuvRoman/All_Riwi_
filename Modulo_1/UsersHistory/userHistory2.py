
def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida al programa."""
    print("Bienvenido al INVENTARIO")
    print("*" * 25)

def obtener_opcion_menu():
    """Muestra el menú y solicita una opción válida al usuario."""
    while True:
        menu_input = input(
            "\n Menu: \n 1. Agregar producto \n 2. Mostrar inventario\n 3. Calcular estadísticas \n 4. Salir \n Elija un numero: "
        )
        try:
            opcion = int(menu_input)
            if 1 <= opcion <= 4:
                return opcion
            else:
                print(
                    "\nDatos erróneos. Elige un número entre 1 y 4. Vuelve a intentarlo..."
                )
        except ValueError:
            print(
                "\nDatos erróneos. Debes ingresar un número entero. Vuelve a intentarlo..."
            )

def agregar_producto(productos):
    """Solicita los datos de un nuevo producto y lo agrega a la lista."""
    print("\n--- Agregar Producto ---")
    
    # 1. Solicitar Nombre
    while True:
        name = input("Ingrese el nombre del producto: ").strip()
        if not name or name.isnumeric():
            print("\nDatos erróneos. Debes ingresar letras y no puede estar vacío. Vuelve a intentarlo...")
        else:
            break

    # 2. Solicitar Precio
    while True:
        precio_input = input("Ingrese el precio del producto: ").strip()
        try:
            precio = float(precio_input)
            if precio >= 0:
                 break
            else:
                print("\nEl precio debe ser un número positivo. Vuelve a intentarlo...")
        except ValueError:
            print("\nDatos erróneos. Debes ingresar un número para el precio. Vuelve a intentarlo...")
            
    # 3. Solicitar Cantidad
    while True:
        cantidad_input = input("Ingrese la cantidad del producto: ").strip()
        try:
            cantidad = int(cantidad_input)
            if cantidad >= 0:
                break
            else:
                print("\nLa cantidad debe ser un número entero no negativo. Vuelve a intentarlo...")
        except ValueError:
            print("\nDatos erróneos. Debes ingresar un número entero para la cantidad. Vuelve a intentarlo...")

    producto = {"nombre": name, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print(f"\n✅ Producto '{name}' agregado correctamente al inventario.")

def mostrar_inventario(productos):
    """Muestra todos los productos registrados en el inventario."""
    print("\n--- Inventario Actual ---")
    if not productos:
        print("No hay productos registrados.")
    else:
        print(f"{'Nombre':<15} | {'Precio':<10} | {'Cantidad':<10}")
        print("-" * 37)
        for producto in productos:
            print(
                f"{producto['nombre']:<15} | {producto['precio']:<10.2f} | {producto['cantidad']:<10}"
            )

def calcular_estadisticas(productos):
    """Calcula y muestra el valor total del inventario y la cantidad total de productos."""
    print("\n--- Estadísticas del Inventario ---")
    if not productos:
        print("No hay productos registrados.")
    else:
        cantidad_total = 0
        valor_total_inventario = 0.0

        for producto in productos:
            # Asegurar que se usen los tipos correctos para los cálculos
            cantidad = int(producto["cantidad"])
            precio = float(producto["precio"])

            cantidad_total += cantidad
            valor_total_inventario += precio * cantidad

        print(f"{'Valor Total Inventario':<25} | {'Cantidad Total de Productos':<10}")
        print("-" * 55)
        print(
            f"€ {valor_total_inventario:<23.2f} | {cantidad_total:<10}"
        )

def ejecutar_inventario():
    """Función principal que ejecuta el bucle del inventario."""
    
    # Lista global para almacenar los productos (lista de diccionarios)
    productos = []
    mostrar_bienvenida()

    while True:
        opcion = obtener_opcion_menu()

        if opcion == 1:
            agregar_producto(productos)
        elif opcion == 2:
            mostrar_inventario(productos)
        elif opcion == 3:
            calcular_estadisticas(productos)
        elif opcion == 4:
            print("\n¡¡Gracias por utilizar el inventario!!, vuelva pronto 👋")
            break  # Sale del bucle while True y finaliza el programa

if __name__ == "__main__":
    ejecutar_inventario()