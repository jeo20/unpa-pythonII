"""
Problema 3: Evaluación de Proyectos
Un profesor tiene las notas de varios proyectos presentados por los estudiantes en diferentes materias.
Calcula el promedio de las notas de cada proyecto y almacena los resultados en una nueva lista llamada promedios_proyectos.

notas_proyectos = [
    [85, 90, 88, 92],  # Proyecto 1
    [78, 82, 80, 85],  # Proyecto 2
    [92, 94, 96, 98]   # Proyecto 3
]

"""

notas_proyectos = [
    [85, 90, 88, 92],  # Proyecto 1
    [78, 82, 80, 85],  # Proyecto 2
    [92, 94, 96, 98]   # Proyecto 3
]

promedios_proyectos = []

for proyecto in notas_proyectos:
    promedio_proyecto = sum(proyecto) / len(proyecto)
    promedios_proyectos.append(promedio_proyecto)
print(promedios_proyectos)