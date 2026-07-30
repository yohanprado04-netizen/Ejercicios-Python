class Usuario:
    def __init__(self,Usuario, Contraseña):
        self.Usuario = Usuario
        self.__Contraseña = Contraseña

User = Usuario("Prado", "praderaos")
print(f"{User.__Contraseña}")