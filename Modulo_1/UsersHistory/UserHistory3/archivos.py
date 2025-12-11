#se crea la funcion para guardar el csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """
    if not inventario:
        print("No se puede guardar: el inventario está vacío.")
        return

    try:
        with open(ruta, "w", encoding="utf-8") as f:
            if incluir_header:
                f.write("nombre,precio,cantidad\n")

            for p in inventario:
                linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
                f.write(linea)

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print("Error al guardar el archivo:", e)


def cargar_csv(ruta):
    """
    Carga un archivo CSV y retorna una lista de productos.
    """
    productos = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        # Validar encabezado
        encabezado = lineas[0].strip()
        if encabezado != "nombre,precio,cantidad":
            print("Encabezado inválido.")
            return []

        for linea in lineas[1:]:
            partes = linea.strip().split(",")

            if len(partes) != 3:
                errores += 1
                continue

            try:
                nombre = partes[0]
                precio = float(partes[1])
                cantidad = int(partes[2])

                if precio < 0 or cantidad < 0:
                    errores += 1
                    continue

                productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

            except ValueError:
                errores += 1

        print(f"Archivo cargado. Filas inválidas omitidas: {errores}")
        return productos

    except FileNotFoundError:
        print("No se encontró el archivo.")
        return []

    except Exception as e:
        print("Error al cargar:", e)
        return []
