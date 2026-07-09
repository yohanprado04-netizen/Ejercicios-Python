tabla = [2,5,8]
contador = 0

tamanio = len(tabla)
print("La cantidad de tablas es: ", tamanio)

while contador < tamanio:
        
        print(f"TABLA DEL {tabla[contador]}")

        for numero in range(1, 13):
                print(f"{tabla[contador]} x {numero} = {tabla[contador] * numero}")
        contador += 1