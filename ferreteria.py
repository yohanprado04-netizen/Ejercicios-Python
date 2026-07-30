almacen = {}
lista_categorias = []


class Producto:
    def __init__(self, Codigo_producto, Nombre, Categoria, Precio, Cantidad):
        self.Codigo_producto = Codigo_producto
        self.Nombre = Nombre
        self.Categoria = Categoria
        self.Precio = Precio
        self.Cantidad = Cantidad

    def mostrar_informacion(self):
        info_pro = {
            "Codigo_producto": self.Codigo_producto,
            "Nombre": self.Nombre,
            "Categoria": self.Categoria,
            "Precio": self.Precio,
            "Cantidad": self.Cantidad
        }
        return info_pro
def almacenar_producto():
    codigo = input("Ingrese el código del producto: ")
    producto_existente = None
    for prod in almacen.values():
        if prod.Codigo_producto == codigo:
            producto_existente = prod
            break
    if producto_existente is not None:
        print(f"El producto '{producto_existente['Nombre']}' ya existe.")
        nueva_cantidad = int(input("Ingrese la cantidad a añadir al stock: "))
        producto_existente["Cantidad"] += nueva_cantidad
        print(f"Stock actualizado. Nueva cantidad total: {producto_existente['Cantidad']}\n")
    else:
        print("Producto no existe. Hay que almacenaarlo.")
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Precio invalido.\n")
        else:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad <= 0:
                print("Cantidad invalida.\n")
            else:
                producto = Producto(codigo, nombre, categoria, precio, cantidad)
                almacen[codigo] = producto
                print("Producto almacenado exitosamente.\n")
                agregar_categoria(categoria)
                return

def agregar_categoria(categoria):
    if categoria not in lista_categorias:
        lista_categorias.append(categoria)


def mostrar_todos_los_productos():
    if not almacen:
        print("No hay productos en el almecen.\n")
    else:
        for producto in almacen.values():
            info = producto.mostrar_informacion()
            print(f"Producto: {info['Nombre']}, Código: {info['Codigo_producto']}, Categoría: {info['Categoria']}, Precio: {info['Precio']}, Cantidad: {info['Cantidad']}\n")
            return
def Mostrar_productos_categoria():
    if not lista_categorias:
        print("No hay categorias registradas.\n")
    else:
        for categoria in lista_categorias:
            print(f"Productos en la categoría '{categoria}':\n")
            for producto in almacen.values():
                if producto.Categoria == categoria:
                    info = producto.mostrar_informacion()
                    print(f"- {info['Nombre']} (Código: {info['Codigo_producto']}, Precio: {info['Precio']:,.2f}, Cantidad: {info['Cantidad']})\n")

def Mostrar_Producto_Costoso():
    if not almacen:
        print("No hay datos para calcular el valor total del inventario.\n") 
    else:
        for producto in almacen.values():
            if producto.Precio == max(p.Precio for p in almacen.values()):
                info = producto.mostrar_informacion()
                print(f"Producto de mayor precio: {info['Nombre']} (Código: {info['Codigo_producto']}, Precio: {info['Precio']:,.2f})\n")
def Total_inventario():
    if not almacen:
            print("No hay datos para calcular el valor total del inventario.\n")
    else:
        for p in almacen.values():
            valor_total = sum(p.Precio * p.Cantidad for p in almacen.values())
        print(f"Valor total del inventario: {valor_total:,.2f}\n")
        return


def buscar_producto():
    if not almacen:
        print("No hay productos.\n")
    else:
        codigo = input("Ingrese el codigo del producto: ")
        for cod in almacen.values():
            if cod.Codigo_producto == codigo:
                info = cod.mostrar_informacion()
                print(f"Producto encontrado: {info['Nombre']} (Código: {info['Codigo_producto']}, Categoría: {info['Categoria']}, Precio: {info['Precio']:,.2f}, Cantidad: {info['Cantidad']})\n")
            else :
                print("Producto no encontrado.\n")           
def eliminar_producto():
    if not almacen:
        print("No hay productos en el almacen.\n")
    else:
        codigo = input("Ingrese el codigo del producto a remover: ")
        for cod in almacen.values():
            if cod.Codigo_producto == codigo:
                del almacen[cod.Codigo_producto]
                print(f"Producto con código {codigo} eliminado exitosamente.\n")
                return

def menu():
    print("Menu de la ferreteria PraderaOS.")
    print("1. Agregar producto.")
    print("2. Buscar producto por codigo.")
    print("3. Actualizar cantidad.")
    print("4. Mostrar todos los productos.")
    print("5. Mostrar productos de una categoria.")
    print("6. Mostrar producto más costoso.")
    print("7. Mostrar total del inventario")
    print("8. Eliminar un producto.")
    print("9. Salir.")

def main():
    while True:
        menu()
        opcion = int(input("Ingresa una opción: "))
        if opcion == 1:
            almacenar_producto()
        elif opcion == 2:
            buscar_producto()
        elif opcion == 3:
            almacenar_producto()
        elif opcion == 4:
            mostrar_todos_los_productos()
        elif opcion == 5:
            Mostrar_productos_categoria()
        elif opcion == 6:
            Mostrar_Producto_Costoso()
        elif opcion == 7:
            Total_inventario()
        elif opcion == 8:
            eliminar_producto()
        elif opcion == 9:
            print("Saliendo del inventario PraderaOS...")
            print("Listo.") 
        else: 
            print("Número no valido. Vuelva a interalo con una de las opciones requeridas.")

if __name__ == "__main__":
    main()
        
        
