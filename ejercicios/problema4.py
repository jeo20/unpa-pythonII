"""
Problema 4: Clasificación de Palabras
Un editor tiene una lista de listas de palabras y necesita filtrar solo las palabras que empiezan 
con una vocal, transformarlas a mayúsculas y almacenarlas en una nueva lista llamada palabras_vocal.


textos = [
    ["hola", "amigo", "editor"],
    ["excelente", "opcion", "unica"],
    ["inteligente", "eficaz", "util"]
]

"""

textos = [
    ["hola", "amigo", "editor"],
    ["excelente", "opcion", "unica"],
    ["inteligente", "eficaz", "util"]
]

palabras_vocal = []

vocales = "aeiou"

for lista in textos:
    for palabra in lista:
        if palabra[0].lower() in vocales:
            palabras_vocal.append(palabra.upper())
print(palabras_vocal)