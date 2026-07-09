#Se requiere calcular el impuesto al valor agregado, de un producto en colombia, el valor del porcentaje es del 19%
#elabore un script que lo calcule

Producto_pre = 25_000
iva = 0.19

NombrePro = str(input("Ingrese nombre del producto: "))
Aumento_Precio = Producto_pre*(1+iva)

print(f"Valor del producto {NombrePro} es de {Aumento_Precio}")