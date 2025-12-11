#se importan las funciones de el archivo servicios
from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas
)

from archivos import guardar_csv, cargar_csv

inventario = []
#Comienza el bucle del menu principal
while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Elige una opción: ")
 
 #Empiezan las condiciones 
    
    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        agregar_producto(inventario, nombre, precio, cantidad)
        print("Producto agregado.")

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        producto = buscar_producto(inventario, nombre)
        if producto:
            print(producto)
        else:
            print("No encontrado.")

    elif opcion == "4":
        nombre = input("Nombre a actualizar: ")
        nuevo_precio = float(input("Nuevo precio: "))
        nueva_cantidad = int(input("Nueva cantidad: "))
        if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
            print("Actualizado.")
        else:
            print("Producto no existe.")

    elif opcion == "5":
        nombre = input("Nombre a eliminar: ")
        if eliminar_producto(inventario, nombre):
            print("Eliminado.")
        else:
            print("Producto no existe.")

    elif opcion == "6":
        stats = calcular_estadisticas(inventario)
        if stats:
            print("\n--- Estadísticas ---")
            print("Unidades totales:", stats["unidades_totales"])
            print("Valor total:", stats["valor_total"])
            print("Más caro:", stats["producto_mas_caro"])
            print("Mayor stock:", stats["producto_mayor_stock"])
        else:
            print("No hay productos.")

    elif opcion == "7":
        ruta = input("Ruta del archivo CSV: ")
        guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = input("Ruta del archivo CSV: ")
        cargado = cargar_csv(ruta)

        if cargado:
            print("¿Sobrescribir inventario actual? (S/N)")
            r = input("> ")
            if r.upper() == "S":
                inventario = cargado
                print("Inventario sobrescrito.")
            else:
                # sumar cantidades y actualizar precios
                for p in cargado:
                    existente = buscar_producto(inventario, p["nombre"])
                    if existente:
                        existente["cantidad"] += p["cantidad"]
                        existente["precio"] = p["precio"]
                    else:
                        inventario.append(p)
                print("Inventario fusionado.")

    elif opcion == "9":
        print("Gracias por utilizar este servicio")
        
        #se cierra el bucle del menu
        break

    else:
        print("Opción inválida.")
