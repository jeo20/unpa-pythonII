"""
Problema 9: Emparejando Datos
Un organizador tiene una lista de nombres y una lista de edades.
Usa comprensión de listas para crear una nueva lista de tuplas que emparejen 
cada nombre con su edad correspondiente.

nombres = ["Juan", "Ana", "Luis"]
edades = [28, 22, 35]

"""

nombres = ["Juan", "Ana", "Luis"]

edades = [28, 22, 35]

nombre_edad = [(nombre, edad) for nombre, edad in zip(nombres, edades)]

print(nombre_edad)