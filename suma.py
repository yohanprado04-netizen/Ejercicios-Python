estudiantes = []
notas = []  # Esto se convertirá en nuestra matriz (lista de listas)
prome = []

cestudiante = int(input("Ingrese cantidad de estudiantes: "))
cnotas = int(input("Ingrese la cantidad de notas a calcular: "))

for stud in range(cestudiante):
    estudiante = str(input(f"\nIngrese nombre del estudiante {stud + 1}: "))
    estudiantes.append(estudiante)
    
    # Creamos una lista vacía para las notas de ESTE estudiante actual (una fila nueva)
    notas_estudiante = []
    snotas = 0  # Reiniciamos la suma para cada estudiante nuevo

    for i in range(cnotas):
        nota = float(input(f"  Ingrese nota {i + 1} de {estudiante}: "))
        notas_estudiante.append(nota)  # Guardamos la nota en su lista individual
        snotas = snotas + nota

    # Guardamos la lista de notas de este alumno dentro de la matriz principal
    notas.append(notas_estudiante)

    # Calculamos y guardamos el promedio independiente de este estudiante
    prom = snotas / cnotas
    prome.append(prom)

# === RECORRIDO E IMPRESIÓN DE RESULTADOS INDEPENDIENTES ===
print("\n" + "="*40)
print("       RESUMEN DE CALIFICACIONES")
print("="*40)

for stud in range(cestudiante):
    print(f"\nEstudiante: {estudiantes[stud]}")
    
    # Recorremos la matriz en la fila de este estudiante para mostrar sus notas
    print(f"Notas: {notas[stud]}") 
    print(f"Promedio: {prome[stud]:.2f}") # :.2f recorta a 2 decimales
    
    # Evaluamos su promedio independiente
    if prome[stud] >= 3:
        print("Estado: APROBADO")
    elif 2.95 <= prome[stud] < 3:
        print("Estado: PENDIENTE")
    else:
        print("Estado: REPROBADO")
        
    # Obtenemos los valores mínimos y máximos de SU lista de notas
    print(f"Nota mínima: {min(notas[stud])}")
    print(f"Nota máxima: {max(notas[stud])}")
    print("-" * 30)
