"""
Problema 10: Filtrado de Cadenas
Una biblioteca tiene una lista de listas de títulos de libros.
Filtra los títulos que tienen más de 5 caracteres y almacénalos en una nueva lista llamada titulos_filtrados.

titulos_libros = [
    ["Cien", "Años", "Soledad"],
    ["Don", "Quijote", "Mancha"],
    ["Rayuela", "Casa", "Muñeca"]
]

"""
titulos_libros = [
    ["Cien", "Años", "Soledad"],
    ["Don", "Quijote", "Mancha"],
    ["Rayuela", "Casa", "Muñeca"]
]

titulos_filtrados = []

for lista in titulos_libros:
    for titulo in lista:
        if len(titulo) > 5:
            titulos_filtrados.append(titulo)
            
print(titulos_filtrados)