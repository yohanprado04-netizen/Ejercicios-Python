#funcion DEF QUE RECIBE PARAMETROS Saldo disponible y saldo a retirar
#Si escribo un saldo negativo, la excepcion me muestre que escriba un saldo valido
#Si el monto a retirar es mayor al saldo, la excepcion muestra saldo insuficiente
#Try except
saldo_disponible = 100_000_000



while True:
    try:
            saldo_a_retirar = float(input("Ingrese lo que quiere retirar: "))
            
            if saldo_a_retirar < 0:
                print("Numero invalido")
            elif saldo_a_retirar > saldo_disponible:
                print("Saldo insuficiente para realizar el retiro.")
            else:
                nuevo_saldo = saldo_disponible - saldo_a_retirar
                print(f"Retiro exitoso. Nuevo saldo: {nuevo_saldo:,.2f}")
            
    except ValueError:
            print("Valor no valido.")





