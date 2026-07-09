#Registrar nombre, precio, cantidad. Calcular el valor total del inventario, 
#Identificar el producto más costoso y economico. por ultimo mostrar un resumen del inventario
#Debe permitir eliminar productos. 

inventario = []

#Menu interactivo
def menu():
    print("Menu:")
    print("1. Consultar inventario.")
    print("2. Agregar productos al inventario.")
    print("3. Eliminar productos.")
    print("4. Salir.")

#Definición para consultar el diccionario
def consultar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
            #Identificar el producto más costoso y económico
            if 'mas_costoso' not in locals() or producto['precio'] > mas_costoso['precio']:
                mas_costoso = producto
            if 'mas_economico' not in locals() or producto['precio'] < mas_economico['precio']:
                mas_economico = producto
    
    print(f"Producto más costoso: {mas_costoso['nombre']} - ${mas_costoso['precio']}")
    print(f"Producto más económico: {mas_economico['nombre']} - ${mas_economico['precio']}")


#Llenar el inventario
def agregar_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
        except ValueError:
            print("Ingrese un valor válido para el precio y la cantidad.")
            continue
        #Agregar productos al inventario con claves
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(producto)
        print(f"Producto {nombre} agregado al inventario.")
        
        continuar = input("¿Quiere seguir agregando productos? (s/n): ")
        if continuar.lower() != 's':
            break

#Eliminar productos del inventario
def eliminar_producto():
    if not inventario:
        print("El inventario está vacío.")
        return
    
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    #FOR PARA RECORRER EL INVENTARIO PARA BUSCAR EL PRODUCTO A ELIMINAR
    for producto in inventario:
        if producto['nombre'].lower() == nombre.lower():
            inventario.remove(producto)
            print(f"Producto {nombre} eliminado del inventario.")
            return
    print(f"No se encontró el producto {nombre} en el inventario.")
    
#Main que me mantiene la estructura de pie 
def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ").upper()
        if opcion == '1':
            consultar_inventario()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            consultar_inventario()
            eliminar_producto()
        elif opcion == '4':
            print("Saliendo del inventario...")
            print("Listo.")
            break
        else:
            print("Opción no válida, selecciona 1, 2, 3 o 4.")
if __name__ == "__main__":
    main()