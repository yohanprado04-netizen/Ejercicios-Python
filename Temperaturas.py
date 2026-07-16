#Registro de temperatura, escriba un programa que registre las temperaturas (en grados C°)
#Tomada durante varios días en la ciudad de Quibdó, el programa debe pedir al usuario cuantos 
#días desea registrar y luego calcular las temperaturas de cada día, al final debe mostrar un 
#pequeño reporte donde muestre temperaturas registradas, temperatura más alta registrada, días 
#más caluroso. Requisitos que se deben tener en cuenta: la temperatura más alta para representar
#en un día caluroso es de 32. 

temperaturas = []
tem = []


while True:
    try:
        Registros_dia = int(input("Ingrese los días que desea registrar: "))
        break
    except ValueError: print("Solo se permiten valores enteros. Vuelve a intentarlo.")

for dia in range(Registros_dia):
    registros = str(input("Ingrese el nombre los días a registrar: "))
    temperaturas.append(registros)
    print(f"Temperatura de {registros} agregada.")

print("Temperaturas agregadas correctamente.\n")

for dia in temperaturas:
    registro_tem = float(input(f"Ingresar la temperatura del {dia}: "))
    tem.append(registro_tem)

print("RESUMEN DE LAS TEMPERATURAS REGISTRADAS.\n")
for i,dia in zip(temperaturas,tem):
    print(f"Temperatura del día {i} es de {dia}°C ")

print(f"Temperatura más alta registrada es de {max(tem)}°C")

for i,dia in zip(temperaturas,tem):
    if dia >= 32:
        print(f"Temperatura del día {i} es muy alta, es de {dia}°C.")
