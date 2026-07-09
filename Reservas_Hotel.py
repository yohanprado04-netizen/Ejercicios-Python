#Variables globales
i = 0
posicion = 0
ingreso_total = 0

#Lista (Diccionario) de reservas
reservas = [
    {"huesped": "Pedro Salcedo", "noches": 3, "tarifaNoche": 120000},
    {"huesped": "Diana Forero", "noches": 7, "tarifaNoche": 95000},
    {"huesped": "Rene Palacios", "noches": 1, "tarifaNoche": 110000},
    {"huesped": "Gloria Serna", "noches": 6, "tarifaNoche": 130000},
    {"huesped": "Marcos Daza", "noches": 2, "tarifaNoche": 105000},
    {"huesped": "Isabel Cano", "noches": 10, "tarifaNoche": 90000}
]

#Desarrollo

#Un ciclo for para recorrer reservas e imprimir el total a pagar de cada huesped
for i in reservas: #Inicio un for para recorrer el dicionario de reservas
    total_pagar = i["noches"] * i["tarifaNoche"] #Linea que me permite calcular el total a pagar de cada huesped
    if i["noches"] > 5: #Evaluo con if si el huesped tiene más de 5 noches
        total_pagar = total_pagar * (1-0.1) #Formula para calcular el descuento directamente
        
    print(f"Total a pagar de {i['huesped']} es de ${total_pagar:,.0f}") #Imprimo el total a pagar de cada huesped

#Ciclo WHILE para recorrer y verificar los huesped que tengan 1 noche apenas
while posicion < len(reservas): #Inicio un WHILE que me permite recorrer el diccionario RESERVAS
    i = reservas[posicion] #Esta linea me permite que i SIMPRE este hubicado en la POSICIÓN de cada huesped
    if i["noches"] == 1: #Evaluamos si la noche de un huesped es el igual 1 
        print(f"\n{i['huesped']} Estancia minima") #Imprimimos los huespued que solo hayan estado una noche con estancia minima
    posicion = posicion + 1 #Variable acumulativa que me permite funcionar el while hasta el numero de reservas

#Ciclo for para recorrer nuevamente y calcular los ingresos totales
for i in reservas: #Inicio un for para recorrer el dicionario de reservas
    total_pagar = i["noches"] * i["tarifaNoche"] #Linea que me permite calcular el total a pagar de cada huesped
    if i["noches"] > 5: #Evaluo con if si el huesped tiene más de 5 noches
        total_pagar = total_pagar * (1-0.1) #Formula para calcular el descuento directamente
    ingreso_total = ingreso_total + total_pagar #Linea que me va almacenar la suma de todos los ingresos

print(f"\nSuma total de todos los ingresos: ${ingreso_total:,.0f}") #Imprimo el total de ingresos

