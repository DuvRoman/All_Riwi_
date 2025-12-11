def mostrarBienvenidaGestion():
    print("Bienvenido al Modulo de Reportes")
    print("*" * 25)

def menuReportes():
    while True:
        menu_input = input(
            "\n Menu de Ventas: \n 1. Top 3 de productos más vendidos\n 2. Reporte por autor \n 3. Ingreso neto y bruto\n 4. Salir al Menú Principal \n Elija un numero: "
        )
        try:
            option = int(menu_input)
            if 1 <= option <= 4:
                return option
            else:
                print(
                    "\nDatos erróneos. Elige un número entre 1 y 4. Vuelve a intentarlo..."
                )
        except ValueError:
            print(
                "\nDatos erróneos. Debes ingresar un número entero. Vuelve a intentarlo..."
            )

def ejecutarReportes():
    while True:
        option = menuReportes()

        if option == 1:
            print("")

        elif option == 2:
           print("")

        elif option == 3:
            print("")
    
        elif option == 4:
            break