productos = []

def cargar_datos():
    try:
        with open("productos.txt", "r") as file:
            for linea in file:  # para recorrer cada linea
                nombre, precio, cantidad = linea.strip().split(",")  # strip para eliminar espacio o salto de linea y split(",") para que se guarden con comitas
                productos.append(
                    {
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad),
                    }
                )
    except FileNotFoundError:
        print("Todavia no se cargaron datos en el archivo productos.txt")

def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Los datos se guardaron correctamente")

def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Ingrese correctamente los valores")

    productos.append(
        {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
    )

def ver_productos():
    if not productos:
        print("No se encontraron productos cargados")
    else:
        for i, producto in enumerate(productos, start=1):  # tupla - enumerate para mostrar el prodcuto con un numero de indice
            print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Ingrese el nombre del producto que se va a actualizat: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto (si no se quiere cambiar deje en blanco): ")
            producto["nombre"] = nuevo_nombre or producto["nombre"]

            try:
                nuevo_precio = input("Ingrese el nuevo precio (o deje en blanco para no cambiarlo): ")
                if nuevo_precio:
                    producto["precio"] = float(nuevo_precio)

                nueva_cantidad = input("Ingrese la nueva cantidad (o deje en blanco para no cambiarlo): ")
                if nueva_cantidad:
                    producto["cantidad"] = int(nueva_cantidad)

                print("Producto actualizado")
                return
            except ValueError:
                print("No se hicieron cambios. Los datos ingresados no son validos")
    print("No se encontró el producto")

def eliminar_producto():
    nombre = input("Ingrese el nombre que se desea eliminar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print("Producto eliminado")
            return
    print("No se encontro el producto")

def menuprincipal():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menuprincipal()
