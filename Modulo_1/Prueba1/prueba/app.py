from gestionInventario import (ejecutar_inventario)
from RegistroConsultaVentas import (ejecutarVentas)
from moduloReportes import (ejecutarReportes)


if __name__ == "__main__":
    libros = [
        {
            "idBook" : 1,
            "titulo" :"Superman",
            "nameAutor" : "Juan Carlos",
            "category" : "Accion",
            "price" : 15.000,
            "discount" : 20,
            "amount" : 20

        },

        {
            "idBook" : 2,
            "titulo" :"Godzilla",
            "nameAutor" : "Armando Ramos",
            "category" : "Accion",
            "price" : 8.000,
            "discount" : 10,
            "amount" : 10

        },

        {
            "idBook" : 3,
            "titulo" :"Harry Potter",
            "nameAutor" : "Soila vaca",
            "category" : "Drama",
            "price" : 15.000,
            "discount" : 5,
            "amount" : 24
        },

            
        {
            "idBook" : 4,
            "titulo" :"Padrinos Magicos",
            "nameAutor" : "Jean Ternera",
            "category" : "Ficción",
            "price" : 16.000,
            "discount" : 10,
            "amount" : 27
        },

        {
            "idBook" : 5,
            "titulo" :"Fast Furious",
            "nameAutor" : "Juan Bautista",
            "category" : "Acción",
            "price" : 35.000,
            "discount" : 5,
            "amount" : 40
        }
    
    ]

    ventas = []

    print("Bienvenido a La Libreria ")
    print("*" * 25)

    while True:
        option = input(
            "\n Menu: \n 1. Gestion del Inventario \n 2. Registro y consulta de ventas\n 3. Módulo de reportes\n 4. Salir\n  Elija un numero: "
        )
        try:
            option = int(option)
            if 1 <= option <= 5:
                option
            else:
                print(
                    "\nDatos erróneos. Elige un número entre 1 y 4. Vuelve a intentarlo..."
                )
        except ValueError:
            print(
                "\nDatos erróneos. Debes ingresar un número entero. Vuelve a intentarlo..."
            )

        if option == 1:
            ejecutar_inventario(libros)
        elif option == 2:
            ejecutarVentas(ventas, libros)
        elif option == 3:
            ejecutarReportes
        elif option == 4:
            break

