cleintes_enero = {"Ana", "Pedro", "Laura", "Carlos"}
cleintes_febrero = {"Laura", "Carlos", "Sofia", "Diego"}

#Formas de hacer la union

union_metodo = cleintes_enero.union(cleintes_febrero)
union_operador = cleintes_enero | cleintes_febrero

print("Union (metodo): ", union_metodo)
print("Union (operador |): ", union_operador)
print(f"Clientes que compraron en AMBOS meses: {len(union_operador)}")