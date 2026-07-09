#Elabore un scrip en python que imprima los bumeros del uno al 10, saltando los pares.

numeros = 0

while numeros < 10:
    numeros += 1 
    if numeros % 2 == 0:
        continue
    print(f"Numero {numeros} impar")
