# Lista para almacenar productos
productos = []
def añadir_producto():
    nombre = input("Introduzca el nombre del producto que desea añadir: ")
    try:
        precio = float(input("Introduzca el precio del producto: "))
        cantidad = int(input("Introduzca la cantidad del producto: "))
    except ValueError:
        print("Error: El precio debe ser un número y la cantidad debe ser un número entero.")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)  

 
    with open("productos.txt", "a") as file:
        file.write(f"{nombre}, {precio}, {cantidad}")
    
    print(f"Se ha añadido el producto '{nombre}' exitosamente.")

def ver_productos(): 
  if not productos:
      print("No hay productos en la lista")
  with open("productos.txt", "r") as file:
      print(file.read())


    

def actualizar_producto():
    ver_productos()
    if not productos:
        return

    try:
        modificar_producto = int(input("Introduzca el número del producto que desea modificar: ")) 
        if modificar_producto < 0 or modificar_producto >= len(productos):
            print("El número del producto no existe.")
            return

        producto_seleccionado = productos[modificar_producto]
        print(f"Producto seleccionado: {producto_seleccionado}")

        print("¿Qué desea modificar?")
        print("1: Nombre")
        print("2: Precio")
        print("3: Cantidad")
        print("4: Cancelar")

        opcion_modificar = input("Elija una opción a modificar: ")
        if opcion_modificar == '1':
            nombre_nuevo = input("Modifique el nombre del producto: ")
            producto_seleccionado["nombre"] = nombre_nuevo
        elif opcion_modificar == '2':
            precio_nuevo = float(input("Modifique el precio del producto: "))
            producto_seleccionado["precio"] = precio_nuevo
        elif opcion_modificar == '3':
            cantidad_nueva = int(input("Modifique la cantidad del producto: "))
            producto_seleccionado["cantidad"] = cantidad_nueva
        elif opcion_modificar == '4':
            print("Modificación cancelada.")
            return
        else:
            print("Opción no disponible.")
            return

        print("Producto modificado exitosamente.")
    except ValueError:
        print("Error: Debe ingresar un número válido para el precio y la cantidad.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado exitosamente.")
            return
    print(f"Producto '{nombre}' no encontrado en el inventario.")

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}s")
    print("Datos guardados exitosamente.")

def cargar_datos():
    # Lógica para cargar los datos desde un archivo
    global productos
    productos = []
    try:
        with open("productos.txt", "r") as read_file:
            for line in read_file:
                line = line.strip()
                if line:  
                    nombre, precio, cantidad = line.split(", ")
                    producto = {
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    }
                    productos.append(producto)
    except FileNotFoundError:
        print("No se encontró el archivo de productos. Se creará uno nuevo al guardar.")



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