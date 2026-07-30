class Usuario:
    def __init__(self,password):
        self.__password = password

user = Usuario("Super secreto.")

print(user._Usuario__password)