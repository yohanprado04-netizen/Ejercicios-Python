#Verificar si numero es par, si es positivo, y si es numero primo. Funcion, que llame las anteriores DEF

numero = float(input(
    
    "Ingrese un numero: "
))

def par(numero):
    if numero % 2 == 0:
        return "Es par"
    else:
        return "No es par"
    
def positivo(numero):
    if numero > 0:
        return "Es positivo"
    else:
        return "No es positivo"

def primo(numero):
    if numero < 2:
        return "No es primo"
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return "No es primo"
    return "Es primo"

def verificar_numero(numero):
    return par(numero), positivo(numero), primo(numero)

print(f"El numero {numero} {verificar_numero(numero)[0]}")
print(f"El numero {numero} {verificar_numero(numero)[1]}")
print(f"El numero {numero} {verificar_numero(numero)[2]}")   