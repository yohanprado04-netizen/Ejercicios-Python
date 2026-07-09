print("Bienvenido, vamos a calcular las notas.")

nombre= str(input("Ingrese nombre del estudiante: "))
prom = ()
lista_notas = []

while True:
    notas_inicial = input("Ingrese una nota (0 a 5) o escriba '-1': ")
    salida = notas_inicial.strip().lower()
    
    if salida == "-1":
        print("Calculando notas...")
        break
        
    try:
        nota = float(notas_inicial)
        
        if 0 <= nota <= 5:
            lista_notas.append(nota)
            print(f" Nota {nota} agregada correctamente.")
        else:
            print("Error: La nota debe estar entre 0 y 5")
            
    except ValueError:
        print("Error: Ingrese un número válido o la palabra '-1'")

prom = float(sum(lista_notas) / len(lista_notas) if lista_notas else 0)
print(f"Promedio final de {nombre} es: {prom}")
print(f"Notas válidas registradas: {len(lista_notas)}")
print("La calificación más alta es: ", max(lista_notas) if lista_notas else "No hay notas válidas")
print("La calificación más baja es: ", min(lista_notas) if lista_notas else "No hay notas válidas")
if prom >= 3:
    print (nombre,", aprobo")
elif (prom == 0):
    print("A espera de notas para promediar")
else:
    print(nombre, "reprobado")
