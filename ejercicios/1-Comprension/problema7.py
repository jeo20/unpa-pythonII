"""
Problema 7: Resumen de Resultados
Una empresa ha registrado las ventas de diferentes productos en varias regiones.
Concatenar todas las listas de ventas en una sola lista llamada ventas_totales 
para obtener un resumen de las ventas.

ventas_regiones = [
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
]

"""
ventas_regiones = [
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
]
ventas_totales = [precio for lista in ventas_regiones for precio in lista]
print(ventas_totales)