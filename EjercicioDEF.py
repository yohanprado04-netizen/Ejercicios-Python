opcion = 0
def suma(suma1, suma2):
    return suma1 + suma2

def resta(resta1, resta2):
    return resta1 - resta2

def multiplicacion(mult1, mult2):
    return mult1 * mult2

def division(div1, div2):
    if div2 == 0:
        return "Error: No se puede dividir entre cero"
    return div1 / div2

print("MENU PRINCIPAL")
print("1 - SUMA")
print("2 - RESTA")
print("3 - MULTIPLICACIONES")
print("4 - DIVISION")

opcion = input("Ingrese numero del menu: ")


if opcion == "1":
    suma1 = int(input("Ingrese número 1: "))
    suma2 = int(input("Ingrese número 2: "))
    total = suma(suma1, suma2)
    print("El resultado de la suma es:", total)

elif opcion == "2":
    resta1 = int(input("Ingrese número 1: "))
    resta2 = int(input("Ingrese número 2: "))
    total = resta(resta1, resta2)
    print("El resultado de la resta es:", total)

elif opcion == "3":
    mult1 = int(input("Ingrese número 1: "))
    mult2 = int(input("Ingrese número 2: "))
    total = multiplicacion(mult1, mult2)
    print("El resultado de la multiplicación es:", total)

elif opcion == "4":
    div1 = int(input("Ingrese número 1: "))
    div2 = int(input("Ingrese número 2: "))
    total = division(div1, div2)
    print("El resultado de la división es:", total)

else:
    print("Opción no válida. Por favor, intente de nuevo.")





    

