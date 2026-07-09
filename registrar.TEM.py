#Registrar la temperatura pidiendola al usuario diarias de Quibdó durante 7 días.
#Calcular el promedio, mostrar la temperatura minima y la maxima
#Se debe mostrar la temperatura y el día en que se registro Lunes Martes Miercoles Jueves Viernes Sabado Domingo.
#Listas o Diccionario para recorrer las personas registradas y sus días.
suma = 0
tempe=[]
temperaturas = {}
dias = ["Lunes", "Martes", "Miercoles", 
        "Jueves", "Viernes", "Sabado", "Domingo"
]

for dia in dias:
    temp = float(input(f"Ingrese la temperatura para el día {dia}: "))
    tempe.append(temp)
    suma = suma + temp
    temperaturas[dia] = temp
print("\nTemperaturas registradas:")
for dia, temperatura in temperaturas.items():
    print(f"La temperatura del {dia} fue de {temperatura}°C")

print(f"El promedio de temperatura es {suma/len(tempe)}°C")
print(f"La temperatura minima es {min(tempe)}°C")
print(f"La temperatura maxima es {max(tempe)}°C")
