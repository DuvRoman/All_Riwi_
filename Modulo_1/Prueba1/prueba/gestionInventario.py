
def mostrarBienvenidaGestion():
    print("\n Bienvenido al Inventario De La Libreria ")
    print("*" * 25)

def menuGestionInventario():
    while True:
        menu_input = input(
            "\n Menu: \n 1. Registrar Libro \n 2. Consultar Librería\n 3. Actualizar Librería \n 4. Eliminar Libro \n 5. Salir al Menu Principal \n Elija un numero: "
        )
        try:
            option = int(menu_input)
            if 1 <= option <= 5:
                return option
            else:
                print(
                    "\nDatos erróneos. Elige un número entre 1 y 4. Vuelve a intentarlo..."
                )
        except ValueError:
            print(
                "\nDatos erróneos. Debes ingresar un número entero. Vuelve a intentarlo..."
            )

def registrarLibro(libros):
    print("\n--- Agregar Libro---")

    while True:
        idBook = input("Ingrese el Id del producto: ").strip()
        try:
            idBook= int(idBook)
            break
        except ValueError:
            print("\nDatos erróneos. Debes ingresar un número entero para la cantidad. Vuelve a intentarlo...")
    
   
    while True:
        titulo = input("Ingrese el Título del Libro: ").strip()
        if not titulo or titulo.isnumeric():
            print("\nDatos erróneos. Debes ingresar letras y no puede estar vacío. Vuelve a intentarlo...")
        else:
            break

    
    while True:
        nameAutor = input("Ingrese el Nombre del Autor: ").strip()
        if not nameAutor or nameAutor.isnumeric():
            print("\nDatos erróneos. Debes ingresar letras y no puede estar vacío. Vuelve a intentarlo...")
        else:
            break    

    while True:
        category = input("Ingrese la Categoría del Libro: ").strip()
        if not category or category.isnumeric():
            print("\nDatos erróneos. Debes ingresar letras y no puede estar vacío. Vuelve a intentarlo...")
        else:
            break 

    while True:
        price= input("Ingrese el Precio del Libro: ").strip()
        try:
            price = float(price)
            if price >= 0:
                 break
            else:
                print("\nEl precio debe ser un número positivo. Vuelve a intentarlo...")
        except ValueError:
            print("\nDatos erróneos. Debes ingresar un número para el precio. Vuelve a intentarlo...")
            

    while True:
        amount = input("Ingrese la Cantidad del Libro en Stock : ").strip()
        try:
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("\nLa cantidad debe ser un número entero no negativo. Vuelve a intentarlo...")
        except ValueError:
            print("\nDatos erróneos. Debes ingresar un número entero para la cantidad. Vuelve a intentarlo...")
    
    while True:
        discount = input("Ingrese la Cantidad de DESCUENTO del Libro en Stock : ").strip()
        try:
            discount = int(discount)
            if discount >= 0:
                break
            else:
                print("\nLa cantidad debe ser un número entero no negativo. Vuelve a intentarlo...")
        except ValueError:
            print("\nDatos erróneos. Debes ingresar un número entero para la cantidad. Vuelve a intentarlo...")
    
    libro = {"idBook": idBook, "titulo": titulo, "nameAutor" : nameAutor, "category": category, "price": price, "discount" : discount, "amount": amount}
    libros.append(libro)
    print(f"\n✅ Libro'{titulo}' agregado correctamente al inventario.")

def consultarInventario(libros):
    print("\n--- Inventario Actual ---")
    if not libros:
        print("No hay libros registrados.")
    else:
        print(f"{'ID':<10} |{'Título':<15} | {'Autor':<10} | {'Categoría':<10}| {'Precio':<10} |{'Descuento':<10}| {'Cantidad en stock':<10} | ")
        print("-" * 37)
        for libro in libros:
            print(
                f"{libro['idBook']:<10} | {libro['titulo']:<15} | {libro['nameAutor']:<15} | {libro['category']:<10}| {libro['price']:<10.3f} |  {libro['discount']:<10}% | {libro['amount']:<10} "
            )


def buscarLibro(libros, idBook):
    for l in libros:
        if l['idBook'] == idBook:
            return l
    return None


def actualizarLibro(libros, idBook, newPrice=None, newAmount=None):
   
    libro = buscarLibro(libros, idBook)
  
    if libro:
        if newPrice is not None:
            libro['price'] = newPrice
        if newAmount is not None:
            libro['amount'] = newAmount

        print(f"{libro['titulo']}")
        libro = {"price": newPrice, "amount": newAmount, "idBook" : idBook, "titulo": libro['titulo'], "nameAutor" : libro['nameAutor'], "category": libro['category'], "amount" : libro['amount'], "discount": libro['discount']}
        libros.append(libro)
        print(f"\n✅ Libro'{idBook}' agregado correctamente al inventario.")
        

def eliminarLibro(libros, idBook):
    libroDelete = buscarLibro(libros, idBook)
    if libroDelete:
        libros.remove(libroDelete)
        print("Libro eliminado exitosamente")
        return True
    return False
        
        

def ejecutar_inventario(libros):
    

    mostrarBienvenidaGestion()

    while True:
        option = menuGestionInventario()

        if option == 1:
            registrarLibro(libros)
        elif option == 2:
            consultarInventario(libros)
        elif option == 3:
            idBook= int(input("Ingrese el Id del libro: "))
            newPrice= float(input("Ingrese el nuevo Precio del libro: "))
            newAmount = int(input("Ingrese la nueva Cantidad del libro: "))
            actualizarLibro(libros, idBook, newPrice=newPrice, newAmount=newAmount)
        elif option == 4:
            idBook= int(input("Ingrese el Id del libro: "))
            eliminarLibro(libros, idBook)
        elif option == 5:
            print("\n¡¡Gracias por utilizar el inventario!!, vuelva pronto 👋")
            break  

