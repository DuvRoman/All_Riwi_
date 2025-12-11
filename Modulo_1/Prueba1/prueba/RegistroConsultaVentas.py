from gestionInventario import *
import datetime


def mostrarBienvenidaGestion():
    print("Bienvenido al Registro de Ventas")
    print("*" * 25)

def menuRegistroVentas():
    while True:
        menu_input = input(
            "\n Menu de Ventas: \n 1. Registrar Venta\n 2. Consultar Ventas \n 3. Salir al Menú Principal \n Elija un numero: "
        )
        try:
            option = int(menu_input)
            if 1 <= option <= 3:
                return option
            else:
                print(
                    "\nDatos erróneos. Elige un número entre 1 y 4. Vuelve a intentarlo..."
                )
        except ValueError:
            print(
                "\nDatos erróneos. Debes ingresar un número entero. Vuelve a intentarlo..."
            )





def registrarVentaLibro(ventas, libros):
    print("\n--- Agregar Venta---")
  
    while True:
        userName = input("Ingrese el Nombre de el Cliente: ").strip()
        if not userName or userName.isnumeric():
            print("\nDatos erróneos. Debes ingresar letras y no puede estar vacío. Vuelve a intentarlo...")
        else:
            break

    while True:
        bookSold = int(input("Ingrese el ID del producto vendido: ").strip())
        try:
            bookSold = int(bookSold)
            if bookSold >= 0:
                break
            else:
                print("\nLa cantidad debe ser un número entero no negativo. Vuelve a intentarlo...")
        except ValueError:
            print("\nDatos erróneos. Debes ingresar un número entero para la cantidad. Vuelve a intentarlo...")

    while True:
        amountSold = input("Ingrese la Cantidad vendida del Libro en Stock : ").strip()
        try:
            amountSold = int(amountSold)
            if amountSold >= 0:
                break
            else:
                print("\nLa cantidad debe ser un número entero no negativo. Vuelve a intentarlo...")
        except ValueError:
            print("\nDatos erróneos. Debes ingresar un número entero para la cantidad. Vuelve a intentarlo...")


    libro = buscarLibro(libros, bookSold)   
    if libro:            

        venta = {"idBook": bookSold, "userName": userName, "bookSold": bookSold,"amountSold": amountSold, "date": datetime}
        ventas.append(venta)
        print(f"\n✅ venta a '{userName}' agregada correctamente al inventario.")
    else:
        print("Id no encontrado.. Intentelo de nuevo..")


def consultarVentas(ventas, libros):
    print("\n--- Inventario Actual de ventas ---")
    if not ventas:
        print("No hay Ventas registradas.")
    else:
        print(f"{'ID':<10} |{'Cliente':<15} | {'Categoría':<10}| {'Precio':<10} |{'Descuento':<10}| {'Cantidad':<10} | ")
        print("-" * 37)
        for venta in ventas:
            print(
                f"{venta['idBook']:<10} |Vendido a:  {venta['userName']:<15} | {venta['bookSold']:<10}| {venta['amountSold']:<10}"
            )

def ejecutarVentas(ventas, libros):


    while True:
        option = menuRegistroVentas()

        if option == 1:
            registrarVentaLibro(ventas, libros)
        elif option == 2:
            consultarVentas(ventas, libros)
        elif option == 3:
            break
        

