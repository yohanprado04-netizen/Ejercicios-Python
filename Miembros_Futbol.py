#Clase padre llamada jugador, metodo describir posisción. Tres clases hijas, Arquero, Defensa, Delantero
#cada clase debe describir su rol.


class Jugador:
    def __init__(self):
        self.posiscion_jugador = None

    def describir_posiscion(self):
        return f"El jugador juega en la posición de {self.posiscion_jugador}"

class Arquero(Jugador):
    def __init__(self):
        super().__init__()
        self.posiscion_jugador = "Arquero"

    def describir_posiscion(self):
        return f"El jugador juega en la posición de {self.posiscion_jugador}. Su rol es evitar que el equipo contrario los golee."

class Defensa(Jugador): 
    
    def __init__(self):
        super().__init__()
        self.posiscion_jugador = "Defensa"

    def describir_posiscion(self):
        return f"El jugador juega en la posición de {self.posiscion_jugador}. Su rol es proteger defender los ataques contrarios."

class Delantero(Jugador):
    def __init__(self):
        super().__init__()
        self.posiscion_jugador = "Delanero"

    def describir_posiscion(self):
        return f"El jugador juega en la posicion de {self.posiscion_jugador}. Su rol es marcar goles al equipo contrario"

while True:
    Buscar_posicion = input("¿Qué posición deseas buscar? (Arquero/Defensa/Delantero) o escribe 'salir': ").lower()

    if Buscar_posicion == "arquero":
        posicion = Arquero()
        print(posicion.describir_posiscion())
    elif Buscar_posicion == "defensa":
        posicion = Defensa()
        print(posicion.describir_posiscion())
    elif Buscar_posicion == "delantero":
        posicion = Delantero()
        print(posicion.describir_posiscion())
    elif Buscar_posicion == "salir":
        break
    else:
        print(f"Opción {Buscar_posicion} no encontrada.")
        