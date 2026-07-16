#Dado las siguientes notas, muestre nota mayor y menor, calcule el promedio, aprobados, reprobados




notas = [4.5,3.8,2.6,1.5,4.5,5.0,5.0,1.5]
aprobados = []
reprobados = []

for i in notas:
    if i >= 3.0:
        aprobados.append(i)
    else:
        reprobados.append(i)

print(f"Nota mayor: {max(notas)}")
print(f"Nota menor: {min(notas)} ")
print(f"Promedio de todas las notas: {sum(notas) / len(notas)}")
print(f"Aprobados: {len(aprobados)}")
print(f"Reprobados: {len(reprobados)}")