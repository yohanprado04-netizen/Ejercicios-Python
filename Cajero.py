
Saldo = 1_000_000



def menu():
    print("Menu:")
    print("1. Consultar saldo.")
    print("2. Retirar dinero.")
    print("3. Salir.")

def consulta_saldo():
    print(f"Su saldo es: ${Saldo}")

def retiro_dinero():
    global Saldo
    retiro = int(input(f"Cuanto desea retirar su saldo es de: ${Saldo}: "))
    if retiro > Saldo:
        print("Fondos insuficientes")
    elif retiro <= 0:
        print("Cantidad inválida")
    else:
        Saldo= Saldo - retiro
        print("Retiro exitoso")


def main():
    intentos_maximos = 3
    acceso_concedido = False

    Guardar_contrasena = input("Ingrese la contraseña que quiere para su cajero: ")
    if len(Guardar_contrasena) > 4:
        Guardar_contrasena = input("Ingrese contraseña nuevamente. Solo 4 digitos: ")

    for intento in range(intentos_maximos):
        contrasena = input("Introduzca la contraseña de acceso: ")
        if contrasena == Guardar_contrasena:
            print("Acceso concedido.\n")
            acceso_concedido = True
            break 
        else:
            intentos_restantes = intentos_maximos - (intento + 1)
            if intentos_restantes > 0:
                print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos.\n")


    if not acceso_concedido:
        print("Cajero bloqueado.")
        return
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            consulta_saldo()
        elif opcion == '2':
            retiro_dinero()
        elif opcion == '3':
            print("Saliendo del programa...")
            print("Listo.")
            break
        else:
            print("Opción no válida, selecciona 1, 2 o 3.")
if __name__ == "__main__":
    main()
        