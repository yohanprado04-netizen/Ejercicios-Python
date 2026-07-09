#elabore un algoritmo que dado dos listas, una lista producto y otra precio, el usiario debe
#llenar ambas listas los maximos de producto a registrar son 5 y debe al final mostrar que productos
#tiene precio inferior a 20mil pesos

producto=[]
precio=[]




for indice in range(5):
    product = input(f"Ingrese el nombre del producto {indice+1} (o 'fin' para terminar): ")
    if product.lower() == 'fin':
        break


prec = int(input(f"Ingrese el precio de {product}: "))

producto.append(product)
precio.append(prec)

print("\n--- Productos con precio inferior a $20,000 ---")
encontrado = False

for i in range(len(producto)):
    if precio[i] <= 20000:
        print(f"Producto: {producto[i]} - Precio: ${precio[i]}")
        encontrado = True


