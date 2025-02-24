"""
Problema 8: Filtrado de Puntuaciones
Un jurado ha registrado las puntuaciones de varios participantes en diferentes categorías.
Filtra las puntuaciones mayores a 7 en cada categoría y calcula la suma de estas puntuaciones filtradas.

puntuaciones = [
    [5, 8, 9, 6],
    [7, 8, 6, 9],
    [6, 9, 8, 5]
]

"""
puntuaciones = [
    [5, 8, 9, 6],
    [7, 8, 6, 9],
    [6, 9, 8, 5]
]
puntuaciones_filtradas = [puntuacion for lista in puntuaciones for puntuacion in lista if puntuacion > 7]
suma_puntuaciones = sum(puntuaciones_filtradas)
print(suma_puntuaciones)