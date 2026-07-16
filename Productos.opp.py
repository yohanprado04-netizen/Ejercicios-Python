#Usted ha sido contratado para trabajar en la tienda de la fundacion a+
#se requiere elaborar un pequeño programa el cual le solicite al usuario el producto
#cantidad, precio adicionalmente le pregunte si es funcionario o estudiante
#si es estudiante, le dara un descuento del 7% si es funcionario descuento del 5%
#el programa debe mostrar al finalizar la compra nombre del producto, valor del producto
#cantidad comprada, subtotal, valor del descuento, tipo de usuario y total a pagar.
#es importante que dicho programa sea realizado mediante clases.

class Producto:
    def __init__(self, producto, cantidad, precio, usuario):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.usuario = usuario.lower()
        
    def calcular_totales(self):
        subtotal = self.cantidad * self.precio
        
        if self.usuario == "estudiante":
            total = subtotal * (1-0.07) 
        elif self.usuario == "funcionario":
            total = subtotal * (1-0.05)
        else:
            total = subtotal  
            
        return subtotal, total

    def impresion(self):
        subtotal, total_pagar = self.calcular_totales()
        print("Nombre del producto: ",self.producto)
        print("Cantidad del producto: ",self.cantidad)
        print(f"Precio del producto: {self.precio:,.2f}")
        print(f"Subtotal del producto: {subtotal:,.2f}")
        print("Tipo de usuario: ",self.usuario.capitalize())
        print(f"Total a pagar con descuento: {total_pagar:,.2f}")


nombre_producto = input("Ingrese el nombre del producto: ")
cant_producto = int(input("Ingrese la cantidad del producto: "))
precio_producto = float(input("Ingrese el precio del producto: "))
tipo_usuario = input("¿Usted es funcionario o estudiante? (Funcionario/Estudiante): ")


Venta_compra = Producto(nombre_producto, cant_producto, precio_producto, tipo_usuario)

Venta_compra.impresion()
