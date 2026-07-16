#Simule el cajero de una tienda, el programa debe ir sumando el precio de los productos que el
#cliente compra, la suma debe hacerse uno por uno hasta que el cliente escriba la palabra fin
#luego debe calcular el total, aplicar un descuento si corresponde y mostrar el recibo.
#reuqisito que debe cumplir, el descueno será del 10% que se aplica solo sí la compra supera
#un valor de 150mil, usar listas, bucles o ciclos mostrar en el recibo nombre del producto,
#cantidad comprada, subotal, total y el descuento aplicado.
cantidad = []
producto = []
precio_producto = []
subtotal = []
total = []
while True:
    try:    
        Producto = str(input("Ingrese el nombre del producto (fin) para terminar. : ")).lower()
        if Producto == "fin":
            print("Saliendo de las compras")
            break
        Cantidad = int(input("Ingrese la cantidad del producto: "))
        Precio = float(input("Ingrese el valor del producto: "))
        Subtotal = float(Cantidad * Precio)
        subtotal.append(Subtotal)
        if Subtotal >=150_000:
            Total = float(Subtotal * (1-0.1))
            total.append(Total)
        else:
            Total = Subtotal
            total.append(Total)
        producto.append(Producto)
        cantidad.append(Cantidad)
        precio_producto.append(Precio)
    except ValueError: print("Ingresa los datos que se te indican.")

for n,c,s,t in zip(producto,cantidad,subtotal,total):
    print(f"Con el producto {n} se compro una cantidad de {c} el cual costo {s:,.2f} y el total a pagar es: {t:,.2f}")