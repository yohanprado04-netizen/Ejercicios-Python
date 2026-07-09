#Elabore un algoritmo en python que le pida al usurario un numero y el algoritmo debe de mostrar su
#respectiva tabla si el numero es mayor que cero 

multiplicar= int(input("Ingrese el numero de multiplicar que desea: "))
if multiplicar <= 0:
    multiplicar= int(input("Ingrese el numero de multiplicar que desea diferente a 0 "))

for indice in range(1, 13):
    resultado = multiplicar * indice 
    print(f"{multiplicar} x {indice} = {resultado}")