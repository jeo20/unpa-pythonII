"""
Problema 2: Filtrando Temperaturas
Un meteorólogo ha registrado las temperaturas diarias en varias ciudades durante una semana.
Utiliza comprensión de listas para crear una nueva lista que contenga solo las temperaturas mayores a 30 grados
de cada ciudad.

temperaturas = [
    [32, 31, 28, 30, 35, 33, 31],  # Ciudad 1
    [29, 27, 25, 26, 32, 30, 29],  # Ciudad 2
    [34, 36, 33, 31, 29, 28, 27]   # Ciudad 3
]

"""

temperaturas = [
    [32, 31, 28, 30, 35, 33, 31],  # Ciudad 1
    [29, 27, 25, 26, 32, 30, 29],  # Ciudad 2
    [34, 36, 33, 31, 29, 28, 27]   # Ciudad 3
]

temperaturas_mayores_30 = []

for ciudad in temperaturas:
    for temperatura in ciudad:
        if temperatura > 30:
            temperaturas_mayores_30.append(temperatura)
print(f"Las temperaturas mayores a 30 grados son: {temperaturas_mayores_30}")
