#def nombre_funcion(parametros)
#toda funcion por lo general devuelve un valor
#Funciones son bloques encapsulados en un metodo que permite realizar  operaciones.
#Se definen con la palabra reservada **def** seguido del **nombre de la funcion ()** y dentro de los parentecis los **parametros**
#Ejemplo: **def saludo(nombre):
#Return sirve para devolver un resultado encapsulado, ejemplo una suma

#Hola Prado
#Normalmente sería 
#print("Hola Prado")


def saludo(nombre,edad):
    int(edad)#en este caso convertimos el valor edad en entero
    print(f"Hola, {nombre} tiene {edad} años")

saludo("Pradera", "18")
