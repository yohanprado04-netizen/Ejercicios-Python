print("Hola Kbra, eres el mejor y nadie te detendrá")

#Dado un listado de numeros enteros recorre la lista con un for e indica con un if/else si
#cada numero es par o impar. Al final muestra cuantos pares e inpares hay en total.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = 0
impares = 0

for numero in numeros:

    if numero % 2 == 0:

        print(f"{numero} es par")

        pares = 1 + pares

    else:

        print(f"{numero} es impar")
        
        impares = 1 + impares

print(f"Numeros pares: {pares}")

print(f"Numeros impares: {impares}")