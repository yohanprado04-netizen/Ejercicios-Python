#Se requiere elaborar un programa para el manejo de una legumbreria que permita mediante un menu
#Realizar  las siguientes acciones: 1, crear categorias. 2, Crear prductos. 3, Registrar clientes
#4, Vender. Las categorias deben contener codigo y nombre, los productos deben tener codigo del producto
# # categoria del prudtcto, nombre del prducto, cantidad y precio, para el caso de los clientes
# debe registrar los datos basicos, para el caso de las ventas debe contener codigo del prducto
# cantidad, subtotal y total. En esta primera etapa debe realizar el registro de los datos mediante
# ingreso por teclado excepto ventas, la información ingresada debe ser almacenada en un fichero


import json

def crear_categoria():
    codigo = input("Ingrese el código de la categoría: ")
    nombre = input("Ingrese el nombre de la categoría: ")
    categoria = {
        "codigo": codigo,
        "nombre": nombre
    }

    try:
        with open("categorias.json", "r") as file:
            lista_categorias = json.load(file)
            
    except (FileNotFoundError, json.JSONDecodeError):
        lista_categorias = []

    lista_categorias.append(categoria)
    with open("categorias.json", "w") as file:
        json.dump(lista_categorias, file, indent=4)
    print("Categoría creada exitosamente.")

def crear_producto():
    codigo_producto = input("Ingrese el código del producto: ")
    
    try:
        with open("productos.json", "r") as file:
            lista_productos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_productos = []

    producto_existente = None
    for prod in lista_productos:
        if prod["codigo_producto"] == codigo_producto:
            producto_existente = prod
            break
    if producto_existente is not None:
        print(f"El producto '{producto_existente['nombre_producto']}' ya existe.")
        nueva_cantidad = int(input("Ingrese la cantidad a añadir al stock: "))
        producto_existente["cantidad"] += nueva_cantidad
        print(f"Stock actualizado. Nueva cantidad total: {producto_existente['cantidad']}")
    
    else:
        categoria_producto = input("Ingrese la categoría del producto: ")
        nombre_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad inicial del producto: "))
        if cantidad <= 0:
            cantidad = int(input("Cantidad no valida. Por favor, ingresar cantidad valida: "))
            return

        precio = float(input("Ingrese el precio del producto: "))
        
        nuevo_producto = {
            "codigo_producto": codigo_producto,
            "categoria_producto": categoria_producto,
            "nombre_producto": nombre_producto,
            "cantidad": cantidad,
            "precio": precio
        }
        lista_productos.append(nuevo_producto)

    with open("productos.json", "w") as file:
        json.dump(lista_productos, file, indent=4)
        
    print("Operación realizada con éxito.\n")


def registrar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    email = input("Ingrese el email del cliente: ")
    cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }

    try:
        with open("clientes.json", "r") as file:
            lista_clientes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_clientes = []
    lista_clientes.append(cliente)
    with open("clientes.json", "w") as file:
        json.dump(lista_clientes, file, indent=4)
    print("Cliente registrado exitosamente.")

def vender():
    codigo_producto = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    
    try:
        with open("productos.json", "r") as file:
            productos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("El archivo de productos no existe o está vacío.")
        return

    producto_vendido = None
    for producto in productos:
        if producto["codigo_producto"] == codigo_producto:
            producto_vendido = producto
            break
            
    if producto_vendido is None:
        print("Producto no encontrado.")
        return
        
    if producto_vendido["cantidad"] < cantidad:
        print("Cantidad insuficiente en stock.")
        return
    
    if cantidad <= 0:
        print("Cantidad no valida, ingresar cantidad dentro del rango.")
        return
        
    subtotal = cantidad * producto_vendido["precio"]
    total = subtotal 
    
    venta = {
        "codigo_producto": codigo_producto,
        "cantidad": cantidad,
        "subtotal": subtotal,
        "total": total
    }
    try:
        with open("ventas.json", "r") as file:
            lista_ventas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_ventas = []
        
    lista_ventas.append(venta)
    with open("ventas.json", "w") as file:
        json.dump(lista_ventas, file, indent=4)

    producto_vendido["cantidad"] -= cantidad
    with open("productos.json", "w") as file:
        json.dump(productos, file, indent=4) 
        
    print(f"Venta realizada exitosamente. Total a pagar: ${total}")


def main():
    while True:
        print("Menú:")
        print("1. Crear categorías")
        print("2. Crear productos")
        print("3. Registrar clientes")
        print("4. Vender")
        print("5. Salir")    
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_categoria()
        elif opcion == "2":
            crear_producto()
        elif opcion == "3":
            registrar_cliente()
        elif opcion == "4":
            vender()
        elif opcion == "5":
            print("Saliendo del programa...")
            print("LISTO.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
if __name__ == "__main__":
    main()

