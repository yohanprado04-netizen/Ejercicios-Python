cleintes_enero = {"Ana", "Pedro", "Laura", "Carlos"}
cleintes_febrero = {"Laura", "Carlos", "Sofia", "Diego"}

#Formas de hacer la intersección

interseccion_metodo = cleintes_enero.intersection(cleintes_febrero)
interseccion_operador = cleintes_enero & cleintes_febrero

print("Intersección (metodo): ", interseccion_metodo)
print("Intersección (operador &): ", interseccion_operador)
print(f"Clientes que compraron en AMBOS meses: {len(interseccion_operador)}")