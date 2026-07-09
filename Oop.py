#class persona: --> Nombre de la clase
#   |
#Palabra reservada

class Persona:
    def __init__(self, nombre,apellido,genero,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad


    def saludo(self):
        print(f"Hola mi nombre es {self.nombre}")

pradera = Persona("Prado", "Palacios", "Masculino", 18)

pradera.saludo()