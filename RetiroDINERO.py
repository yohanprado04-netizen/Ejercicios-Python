#funcion QUE RECIBE PARAMETROS Saldo disponible y saldo a retirar
#Si escribo un saldo negativo, la excepcion me muestre que escriba un saldo valido
#Si el monto a retirar es mayor al saldo, la excepcion muestra saldo insuficiente
#Try except
saldo_disponible = 1_000_00
try:
    monto_retirar = float(input("Ingrese el monto a retirar: "))
    if monto_retirar > saldo_disponible:
        raise ValueError("Saldo insuficiente.")
    
    saldo_final = saldo_disponible - monto_retirar
    print(f"Retiro exitoso. Su saldo final es: {saldo_final}")
except ValueError:
    print(f"Error: ingresa un monto valido.")