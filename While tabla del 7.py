#Cree un algoritmo que cree la tabla del 7 usando while y ahora que sea del 7 al 9

Tabla = 7

while Tabla <= 9:
    print(f"Tabla del {Tabla}")
    contador = 1 
    
    while contador <= 12:
        resultado = Tabla * contador
        print(f"{Tabla} x {contador} = {resultado}")
        contador = contador + 1
        
    Tabla = Tabla + 1 
    print() 



    