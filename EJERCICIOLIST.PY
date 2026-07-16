#Crea un programa que me permita gestionar los nombres de 5 estudiantes de una lista
#Luego el programa debe: Mostrar la lista completa, mostrar el ultimo y primer estudiante
#Mostrar cuantos estudiantes hay registrados

Nombre_estudiante = []

while True:
    estudiante = input("Ingrese nombre de los estudiantes (salir) para salir: ").lower()

    if estudiante == "salir":
        print("Resumen estudiantes...")
        print("Listo.\n")
        break 
    Nombre_estudiante.append(estudiante)

print(f"Lista completa: {Nombre_estudiante}")
print(f"Primer estudiante: {Nombre_estudiante[0]}")
print(f"Último estudiante: {Nombre_estudiante[-1]}")
print(f"Hay {len(Nombre_estudiante)} registrados.")