

def menu():
    print("Seleccione la operación.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    

def suma(n1,n2):
    return print(f"La suma de {n1} y {n2} es: {n1 + n2}")

def resta(n1,n2):
    return print(f"La resta de {n1} y {n2} es: {n1 - n2}")

def multiplicacion(n1,n2):
    return print(f"La multiplicación de {n1} y {n2} es: {n1 * n2}")

def division(n1,n2):
    if n2 != 0:
        return print(f"La multiplicación de {n1} y {n2} es: {n1 / n2}")
    else:
        return "Error: División por cero no permitida."

def main():
    while True:
        n1 = float(input("Ingrese un numero: "))
        n2 = float(input("Ingrese otro numero: "))
        menu()
        opcion = input("Seleccione una opción: ").upper()
        if opcion == '1':
            suma(n1,n2)
        elif opcion == '2':
            resta(n1,n2)
        elif opcion == '3':
            multiplicacion(n1,n2)
        elif opcion == '4':    
            division(n1,n2)
        elif opcion == '5':
            print("Saliendo de la calculadora...")
            print("Listo.")
            break
        else:
            print("Opción no válida, selecciona 1, 2, 3, 4 o 5.")
if __name__ == "__main__":
    main()