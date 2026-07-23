#Crear una clase base llamada empleados con dos atributos, nombres y salario base, y un metodo
#Llamado calcular salario, dos clases hijas 1. Emplado administrativo 2. Empleado docente
#Cada una de esas dos clases hijas debe sobrescribir el metodo principal que es calcular salario
#debe aplicar bonificaciones según tipo de empleado. Requisitos, que se muestre el salario final
#independientemente del tipo de empleado. El calcular salario de cada una de las clases hijas debe ser diferentes

class Empleados:
    def __init__(self, nombres, salario_base):
        self.nombres = nombres
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class Empleado_administrativo(Empleados):
    def __init__(self, nombres, salario_base, bonificaciones):
        super().__init__(nombres, salario_base)
        self.bonificaciones = bonificaciones

    def calcular_salario(self):
        return self.salario_base + self.bonificaciones

class Empleado_docente(Empleados):
    def __init__(self, nombres, salario_base, auxilio_transporte):
        super().__init__(nombres, salario_base)
        self.auxilio_transporte = auxilio_transporte

    def calcular_salario(self):
        return self.salario_base + self.auxilio_transporte


Empleado_admin = Empleado_administrativo("Yohan Prado", 5_000_000, 2_000_000)
Empleado_doc = Empleado_docente("Andres Palacios", 2_000_000,500_000)

print(f"Salario de {Empleado_admin.nombres} es de ${Empleado_admin.calcular_salario():,.2f}")
print(f"Salario de {Empleado_doc.nombres} es de ${Empleado_doc.calcular_salario():,.2f}")              