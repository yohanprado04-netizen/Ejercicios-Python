#Elabore un script en python usando el while que muestre los primeros 12 numeros pares.

while True:
    numero = 1
    contador = 0
    while contador < 12:
        if numero % 2 == 0:
            print(numero)
            contador += 1
        numero += 1
    break   

