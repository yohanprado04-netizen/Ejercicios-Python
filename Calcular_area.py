#Elabore un menu que me permit realizar el calculo del area de: circulo, triangulo, cuadrado, cilindro
#Recatangulo y trapecio, aplicando los principios de funciones
import math

def llenar_lista(): 
    num1 = float(input("Ingrese valor numero 1 a calcular: "))
    num2 = float(input("Ingrese valor numero 2 a calcular: "))
    return num1, num2

def area_circulo(radio=None):   
    if radio is None:
        print("No has ingresado datos previos.")
        radio, _ = llenar_lista() 
    resultado = math.pi * (radio ** 2)   
    print(f"El área del círculo es: {resultado:.2f}\n")
    return resultado

def area_triangulo(base=None, altura=None):
    if base is None or altura is None:
        print("No has ingresado datos previos.")
        base, altura = llenar_lista()
    resultado = (base * altura) / 2
    print(f"El área del triángulo es: {resultado:.2f}\n")
    return resultado

def area_cuadrado(lado=None):
    if lado is None:
        print("No has ingresado datos previos.")
        lado, _ = llenar_lista()
    resultado = lado ** 2
    print(f"El área del cuadrado es: {resultado:.2f}\n")
    return resultado

def area_cilindro(radio=None, altura=None): 
    if radio is None or altura is None:
        print("No has ingresado datos previos.")
        radio, altura = llenar_lista()
    area_lateral = 2 * math.pi * radio * altura
    area_bases = 2 * math.pi * (radio ** 2)
    resultado = area_lateral + area_bases
    print(f"El área total del cilindro es: {resultado:.2f}\n")
    return resultado

def area_rectangulo(base=None, altura=None):
    if base is None or altura is None:
        print("No has ingresado datos previos.")
        base, altura = llenar_lista()
    resultado = base * altura
    print(f"El área del rectángulo es: {resultado:.2f}\n")
    return resultado

def area_trapecio(base_mayor=None, base_menor=None):
    if base_mayor is None or base_menor is None:
        print(" No has ingresado datos previos para las bases.")
        base_mayor, base_menor = llenar_lista()
    else:
        print("Usando los valores guardados como bases.")
    altura = float(input("Ingrese la altura del trapecio: "))
    resultado = ((base_mayor + base_menor) * altura) / 2
    print(f"El área del trapecio es: {resultado:.2f}\n")
    return resultado

def menu():
    print("MENÚ")
    print("1. Llenar números a calcular")
    print("2. Calcular area del circulo")
    print("3. Calcular area del triangulo")
    print("4. Calcular area del cuadrado")
    print("5. Calcular area del cilindro")
    print("6. Calcular area del rectangulo")
    print("7. Calcular area del trapecio")
    print("8. Salir")

def main():
    n1, n2 = None, None
    
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        print("")
        
        if opcion == '1':
            n1, n2 = llenar_lista()
            print("¡Datos guardados con éxito!\n")
        elif opcion == '2':
            area_circulo(n1)
        elif opcion == '3':
            area_triangulo(n1, n2)
        elif opcion == "4":
            area_cuadrado(n1)
        elif opcion == "5":
            area_cilindro(n1, n2)
        elif opcion == "6":
            area_rectangulo(n1, n2)
        elif opcion == "7":
            area_trapecio(n1, n2)
        elif opcion == "8":
            print("Saliendo del programa...")
            print("Listo.")
            break
        else:
            print("Opción no válida, selecciona un número del 1 al 8.\n")

if __name__ == "__main__":
    main()
