cleintes_enero = {"Ana", "Pedro", "Laura", "Carlos"}
cleintes_febrero = {"Laura", "Carlos", "Sofia", "Diego"}

#Formas de hacer la union

diferencia_sime_metodo = cleintes_enero.symmetric_difference(cleintes_febrero)
diferencia_sime_operador = cleintes_enero ^ cleintes_febrero

print("Dieferncia simetrica (metodo): ", diferencia_sime_metodo)
print("Diferencia simetrica (operador ^): ", diferencia_sime_operador)
print(f"Verificación manual (Unión - intersección)")
verificación = (cleintes_enero | cleintes_febrero) - (cleintes_enero & cleintes_febrero)
print(verificación)