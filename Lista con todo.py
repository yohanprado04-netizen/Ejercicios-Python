#Elabore un algoritmo que dado un menu con 3 opciones realice lo siguiente
#Opción A: Rellenar una lista con valores
#Opción B: Mostrar suma de todos los valores de la lista, valor mayor, valor menor y el promedio
#Opción C: Mostrar la tabla de multiplicar de los elemntos que estan en la lista

def llenar_lista(): 
    lista = []
    while True:
        valor = input("Ingrese un valor para la lista o 'fin' para terminar: ")
        if valor.lower() == 'fin':
            break
        try:
            numero = int(valor)
            lista.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return lista

def mostrar_estadisticas(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
        return
    suma = sum(lista)
    valor_mayor = max(lista)
    valor_menor = min(lista)
    promedio = suma / len(lista)
    print(f"Suma: {suma}")
    print(f"Valor mayor: {valor_mayor}")
    print(f"Valor menor: {valor_menor}")
    print(f"Promedio: {promedio}")

def tabla_multiplicar(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
        return
    for numero in lista:
        print(f"Tabla de multiplicar del {numero}:")
        for indice in range(1, 11):
            print(f"{numero} x {indice} = {numero * indice}")
        print()

def menu():
    print("Menu:")
    print("A. Rellenar una lista con valores")
    print("B. Mostrar estadísticas de la lista")
    print("C. Mostrar la tabla de multiplicar de los elementos de la lista")
    print("D. Salir")

def main():
    lista = []
    while True:
        menu()
        opcion = input("Seleccione una opción: ").upper()
        if opcion == 'A':
            lista = llenar_lista()
        elif opcion == 'B':
            mostrar_estadisticas(lista)
        elif opcion == 'C':
            tabla_multiplicar(lista)
        elif opcion == 'D':
            print("Saliendo del programa...")
            print("Listo.")
            break
        else:
            print("Opción no válida, selecciona A, B, C o D.")
if __name__ == "__main__":
    main()