Tarifa_base = 45_000
Des_estudiantes = 0.2
Des_adulto_mayor = 0.3
Carga_libre_KG = 10
Precio_KG_extra = 1_500
Cupo_maximo = 12 

class Pasajeros:
    def __init__(self, nombre, edad, tipo, carga_kg):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo.lower()  
        self.carga_kg = carga_kg

    def calcular_descuento(self):
        if self.edad >= 60:
            return Des_adulto_mayor
        elif self.tipo == "estudiante":
            return Des_estudiantes
        else:
            return 0.0

    def calcular_recargo(self):

        if self.carga_kg > Carga_libre_KG:
            kg_extras = self.carga_kg - Carga_libre_KG
            return kg_extras * Precio_KG_extra
        return 0

    def Calcular_total(self):
        recargo = self.calcular_recargo()
        
        if self.edad < 5:
            return recargo
        
        descuento = self.calcular_descuento()
        costo_pasaje = Tarifa_base * (1 - descuento)
        return costo_pasaje + recargo

    def __str__(self):

        total = self.Calcular_total()
        return f"Pasajero: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo.capitalize()}, Total a pagar: ${total:,.2f}"


class Lancha:
    def __init__(self, Nombre_lancha, destino):
        self.Nombre_lancha = Nombre_lancha
        self.destino = destino
        self.pasajeros = [] 

    def registrar_pasajeros(self, pasajero):
        if len(self.pasajeros) < Cupo_maximo:
            self.pasajeros.append(pasajero)
            return True
        return False

    def cupos_disponbles(self):
        return Cupo_maximo - len(self.pasajeros)
    
    def total_recaudado(self):
        total = 0
        for p in self.pasajeros:
            total += p.Calcular_total()  
        return total

    def buscar(self, Nombre_a_buscar):
        for p in self.pasajeros:
            if p.nombre.lower() == Nombre_a_buscar.lower():
                return p  
        return None

    def reporte(self):
        print(f"\nReporte de la lancha {self.Nombre_lancha.upper()}.")
        print(f"Destino de la lancha {self.destino.upper()}")
        print(f"Cupos ocupados: {len(self.pasajeros)} de {Cupo_maximo}")

        if not self.pasajeros:
            print("No hay pasajeros registrados.")
            return
        
        suma_edades = 0
        can_estudiantes = 0
        can_generales = 0

        print("\nLista de pasajeros:")
        for p in self.pasajeros:
            print(f"- {p}")
            suma_edades += p.edad
            if p.tipo == "estudiante":
                can_estudiantes += 1
            else:
                can_generales += 1

        promedio_edad = suma_edades / len(self.pasajeros)
        costo_pasaje = self.total_recaudado()

        print(f"\nReporte del viaje:")
        print(f"- Total Recaudado: ${costo_pasaje:,.2f}")
        print(f"- Promedio de Edad: {promedio_edad:.1f} años")
        print(f"- Pasajeros Estudiantes: {can_estudiantes}")
        print(f"- Pasajeros Generales: {can_generales}\n")


def menu():
    print("Menu:")
    print("1. Registrar pasajeros.")
    print("2. Ver reporte del viaje.")
    print("3. Buscar pasajeros.")
    print("4. Zapar (salir).")

def main():
    nombre_l = input("Ingrese el nombre de la lancha: ").strip()
    destino_l = input("Ingrese el destino del viaje: ").strip()
    
    mi_lancha = Lancha(nombre_l, destino_l)
    print(f"Lancha '{nombre_l}' con ruta a '{destino_l}' lista para registrar y zarpar.\n")

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            print("\nRegistrar pasajeros.")
            if mi_lancha.cupos_disponbles() == 0:
                print("Cupos llenos. Gracias por preferirnos.\n")
                continue
                
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            tipo = input("Tipo (general o estudiante): ")
            carga = float(input("Carga en KG: "))
            
            p = Pasajeros(nombre, edad, tipo, carga)
            if mi_lancha.registrar_pasajeros(p):
                print("Pasajero registrado con éxito.\n")
            else:
                print("No se pudo registrar.\n")
                
        elif opcion == '2':
            mi_lancha.reporte()
            
        elif opcion == '3':
            print("\nBuscar pasajeros.")
            nombre_b = input("Nombre a buscar: ")
            encontrado = mi_lancha.buscar(nombre_b)
            if encontrado:
                print(f"\nPasajero {encontrado} encontrado\n")
            else:
                print(f"\nPasajero {nombre_b.capitalize()} no encontrado.\n")
                
        elif opcion == '4':
            print("Saliendo del programa...")
            print("Listo.")
            break
        else:
            print("\nOpción no válida.\n")

if __name__ == "__main__":
    main()
