columna_reporte_norte = {
    "id_cliente", "nombre", "ciudad", "monto_venta", 
    "fecha", "producto", "descuento_aplicado"
}

columna_reporte_sur = {
    "id_cliente", "nombre", "monto_venta", 
    "fecha", "producto", "canal_venta", "vendedor"
}

#Pregunta 1: ¿Qué columnas tiene AMBOS reportes?
columnas_comunes = columna_reporte_norte.intersection(columna_reporte_sur)
print("Columnas comunes: ", columnas_comunes)

#Pregunta 2: ¿Qué columnas están en el reporte Norte pero NO en el Sur?
solo_en_norte = columna_reporte_norte.difference(columna_reporte_sur)
print("Solo en norte: ", solo_en_norte)

#Pregunta 3: ¿Qué columnas están en el reporte Sur pero NO en el Norte
solo_en_sur = columna_reporte_sur-columna_reporte_norte
print("Solo en sur: ", solo_en_sur)

#Pregunta 4: ¿Cuantas columnas tendría una tabla que combine ambos reportes?
todas_columnas = columna_reporte_norte | columna_reporte_sur
print(f"Columnas en tabla combinada: {len(todas_columnas)}")
