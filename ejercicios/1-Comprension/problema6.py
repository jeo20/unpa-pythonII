"""
Problema 6: Mejor Rendimiento
Un equipo de desarrolladores ha registrado los tiempos de ejecución de diferentes algoritmos en varias pruebas.
Encuentra el mejor tiempo de ejecución (el menor) de cada algoritmo y 
almacena estos tiempos en una nueva lista llamada mejores_tiempos.

tiempos_ejecucion = [
    [0.5, 0.6, 0.55],
    [0.8, 0.75, 0.78],
    [1.2, 1.1, 1.15]
]

"""

tiempos_ejecucion = [
    [0.5, 0.6, 0.55],
    [0.8, 0.75, 0.78],
    [1.2, 1.1, 1.15]
]

mejores_tiempos = []


for i in tiempos_ejecucion:
    mejores_tiempos.append(min(i))
print(f"Los mejores tiempos de ejecución son: {mejores_tiempos}")
