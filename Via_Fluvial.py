
class Envio:
    def __init__(self, remitente, destinatario, producto, peso):
        self.remitente = remitente
        self.destinatario = destinatario
        self.producto = producto
        self.peso = peso

    def calcular_total(self):
        tarifa_estandar = 5 
        valor_kilo_adicional = 5000 
        if self.peso <= tarifa_estandar:
            return 0 
        else:
            kilos_adicionales = self.peso - tarifa_estandar
            return kilos_adicionales * valor_kilo_adicional

    def mostrar_envio(self):
        total_a_pagar = self.calcular_total()
        envio_info = {
            "Remitente": self.remitente,
            "Destinatario": self.destinatario,
            "Producto": self.producto,
            "Peso (kg)": self.peso,
            "Total a pagar ": total_a_pagar
        }
        return envio_info


def menu():
    print("Registro de Envíos Vía Fluvial")
    print("1. Registrar un envío")
    print("2. Buscar datos de envio")
    print("3. Salir")

def main():
    envios = []
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            remitente = input("Ingrese el nombre del remitente: ")
            destinatario = input("Ingrese el nombre del destinatario: ")
            producto = input("Ingrese el nombre del producto: ")
            peso = float(input("Ingrese el peso del producto (kg): "))
            envio = Envio(remitente, destinatario, producto, peso)
            envios.append(envio)
            print("Envío registrado exitosamente.\n")
        elif opcion == '2':
            if not envios:
                print("No hay envíos registrados.\n")
                continue
            for i, envio in enumerate(envios):
                envio_info = envio.mostrar_envio()
                print(f"Envío {i + 1}:")
                for data, data1 in envio_info.items():
                    print(f"{data}: {data1}")
                print()
        elif opcion == '3':
            print("Saliendo de Via Fluvial.")
            break
        else:
            print("Opción no valida, intente nuevamente.\n")
if __name__ == "__main__":
    main()