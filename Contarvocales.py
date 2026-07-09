palabra = str(input("Ingrese la palabra que desea contar sus vocales: "))
vocales = 0
for vocal in palabra:
    if vocal.lower() in "aeiou":
        vocales += 1
print(f"La palabra {palabra} tiene {vocales} vocales")