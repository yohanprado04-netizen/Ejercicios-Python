multiplicar= int(input("Ingrese el numero de multiplicar que desea: "))

for indice in range(1, 13):
    resultado = multiplicar * indice 
    print(f"{multiplicar} x {indice} = {resultado}")