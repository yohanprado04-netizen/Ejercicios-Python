def menu():
    print("MENU PRINCIPAL")
    print("1 - SUMA")
    print("2 - RESTA")
    print("3 - MULTIPLICACIÓN")
    print("4 - DIVISIÓN")
    print("5 - SALIR")
    opcion = input("Ingrese una opción: ")
    return opcion


def sumar(n1, n2):
    return n1 + n2


def restar(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    if n2 == 0:
        return "Error: no se puede dividir entre cero"
    return n1 / n2


def obtener_numeros():
    """Solicita dos números al usuario"""
    try:
        valor1 = int(input("Ingrese Número 1: "))
        valor2 = int(input("Ingrese Número 2: "))
        return valor1, valor2
    except ValueError:
        print("Error: Ingrese números válidos")
        return None, None


def main():
    """Loop principal de la calculadora"""
    while True:
        opcion = menu()
        
        # Validar opción
        if opcion not in ["1", "2", "3", "4", "5"]:
            print("Opción no válida. Intente de nuevo.")
            continue
        
        # Salir del programa
        if opcion == "5":
            print("\n¡Gracias por usar la calculadora!")
            break
        
        # Obtener números
        valor1, valor2 = obtener_numeros()
        
        if valor1 is None or valor2 is None:
            continue
        
        # Ejecutar operación
        if opcion == "1":
            resultado = sumar(valor1, valor2)
            print(f"Resultado: {valor1} + {valor2} = {resultado}\n")

        elif opcion == "2":
            resultado = restar(valor1, valor2)
            print(f"Resultado: {valor1} - {valor2} = {resultado}\n")

        elif opcion == "3":
            resultado = multiplicar(valor1, valor2)
            print(f"Resultado: {valor1} × {valor2} = {resultado}\n")

        elif opcion == "4":
            resultado = dividir(valor1, valor2)
            print(f"Resultado: {valor1} ÷ {valor2} = {resultado}\n")
        
        # El menú se muestra automáticamente en el siguiente ciclo del while


# Ejecutar programa
if __name__ == "__main__":
    main()