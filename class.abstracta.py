from abc import ABC, abstractmethod


class Vicioso(ABC):
    
    @abstractmethod
    def Drogarse():
        return

class Homeless(Vicioso):
    def __init__(self, nombre,saldo):
        self.nombre = nombre
        self.saldo = saldo

    def Drogarse():
        print("consume cualquiera")
def ganar_dinero(self):
    if self.saldo <= 0:
        Robado = float(input("¿Cuanto robo?"))