print("Bienvenido a la calculadora de precio")
print("*" * 40)

entrada = input("Quieres ingresar datos (si / no): ")

while entrada.lower() == "si":
    while True:
        NombreDelProducto = input("Ingresa el nombre del producto: ")
        if NombreDelProducto.isnumeric() or NombreDelProducto == "":
            print("Dato erróneo... el nombre debe contener solo letras.\n")
            
        else:
            break


    while True:
        precio= input("Ingresa el precio de el producto: ")
        try:
            precio = float(precio)
            break
        except ValueError:
            print("Datos erroneos, solo se pueden ingresar numeros.. Vuelve a intentarlo\n")
            

    while True:
        cantidad= input("Ingresa la cantidad de el producto: ")
        try:
            cantidad = int(cantidad)
            break
        except ValueError:
            print("Datos erroneos, solo se pueden ingresar numeros... vuelve a intentarlo\n")
    costoTotal= precio * cantidad

    print(f"\nProducto: {NombreDelProducto} | Precio: {precio:.3f} | Cantidad:{cantidad} | Total: {costoTotal:.3f} ")
    entrada = input("Quieres ingresar datos (si / no): ")

print("Gracias por su compra, vuelva pronto\n")  