class Metodo_Pago:
    def __init__(self):
        self.metodo_pago = None

    def procesar_pago(self,monto):
        self.monto = monto

class Pago_Efectivo(Metodo_Pago):
    def __init__(self):
        super().__init__()
        self.metodo_pago = "Efectivo"

    def procesar_pago(self, monto):
        super().procesar_pago(monto)
        print(f"Procesando pago en {self.metodo_pago} por un monto de ${self.monto:,.2f}")
        print(f"Valido para pagar. Debe pagar {self.monto:,.2f} cualquiera de las 5 mesas disponibles.")

class Pago_Transferencia(Metodo_Pago):
    def __init__(self):
        super().__init__()
        self.metodo_pago = "Transferencia"

    def procesar_pago(self, monto):
        super().procesar_pago(monto)
        print(f"Procesando pago en {self.metodo_pago} por un monto de ${self.monto:,.2f}")
        print(f"Debe depositar en la cuenta 912-968799-49 ahorro, en un limite de tiempo de 2 horas.")

class Pago_Tarjeta(Metodo_Pago):
    def __init__(self):
        super().__init__()
        self.metodo_pago = "Tarjeta"

    def procesar_pago(self, monto):
        super().procesar_pago(monto)
        while True:
            tarjeta  = input("Ingrese numero de tarjeta: ")
            pin = input("Ingrese pin de la tarjeta: ")
            cvc = input("Ingrese cvc de la tarjeta: ")
            if len(pin) > 4:
                print("Pin incorrecto.")
            elif len(cvc) > 3:
                print("cvc incorrecto.")
            else:
                print(f"Procesando pago en {self.metodo_pago} por un monto de ${self.monto:,.2f}")
            break

elegir_pago = input("¿Por donde desea hacer el pago? (Transferencia/Efectivo/Tarjeta): ").lower()
monto_a_pagar = float(input("Ingrese el valor a pagar: "))

if elegir_pago == "efectivo":
    pago = Pago_Efectivo()
    pago.procesar_pago(monto_a_pagar)
elif elegir_pago == "transferencia":
    pago = Pago_Transferencia()
    pago.procesar_pago(monto_a_pagar)
elif elegir_pago == "tarjeta":
    pago = Pago_Tarjeta()
    pago.procesar_pago(monto_a_pagar)
else:
    print("Método de pago no válido.")