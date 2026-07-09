cleintes_enero = {"Ana", "Pedro", "Laura", "Carlos"}
cleintes_febrero = {"Laura", "Carlos", "Sofia", "Diego"}

#Clientes que estuvieron en Enero pero no en Febrero

solo_enero_metodo = cleintes_enero.difference(cleintes_febrero)
solo_enero_operador = cleintes_enero - cleintes_febrero

solo_febrero = cleintes_febrero - cleintes_enero

print("Diferencia (metodo): ", solo_enero_metodo)
print("Diferencia (operador |): ", solo_enero_operador)
print()
print(f"¿Son igual enero u febrero?: {solo_enero_metodo == solo_febrero}")