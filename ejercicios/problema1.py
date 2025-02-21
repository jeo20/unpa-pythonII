"""
Problema 1: Análisis de Ventas
Una tienda tiene las ventas diarias de diferentes productos almacenadas en una lista de listas. 
Cada sublista representa las ventas de un producto durante una semana (7 días). 
Calcula la venta total de cada producto durante la semana y almacena los resultados en una nueva lista 
llamada ventas_totales.

ventas = [
    [150, 200, 250, 300, 350, 400, 450],  # Producto 1
    [75, 100, 125, 150, 175, 200, 225],   # Producto 2
    [30, 60, 90, 120, 150, 180, 210]      # Producto 3
]
"""
ventas = [
    [150, 200, 250, 300, 350, 400, 450],  # Producto 1
    [75, 100, 125, 150, 175, 200, 225],   # Producto 2
    [30, 60, 90, 120, 150, 180, 210]      # Producto 3
]

ventas_totales = []

for producto in ventas:
    ventas_totales.append(sum(producto))
    
print(f"El total de ventas del primer producto es: {ventas_totales[0]}\n")
print(f"El total de ventas del segundo producto es: {ventas_totales[1]}\n")
print(f"El total de ventas del tercer producto es: {ventas_totales[-1]}\n")