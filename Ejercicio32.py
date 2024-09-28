"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  18-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que registra las calificaciones de varias materias y calcular su promedio """
# En python los arreglos se conocen como: listas.
materias = [
    "Cálculo Diferencial",
    "Fundamentos de Programación",
    "Química",
    "Fundamentos de investigación",
    "Matemáticas Discretas",
    "Desarrollo Sustentable"
]

calificaciones = []
promediosMaterias = [0] * 6
promedioGeneral = 0

# Aqui guardamos todas las calificaciones de las materias
for i in range(6):
    # Entrada de datos
    print("Calificación", materias[i])
    califs = []
    for j in range(5):
        calificacion = float(input("Unidad {}: ".format(j + 1)))
        # Guardamos las caliifcaciones en otra lista
        califs.append(calificacion)
        promediosMaterias[i] += calificacion
    calificaciones.append(califs)
    promediosMaterias[i] /= 5
    promedioGeneral += promediosMaterias[i]
    print("")

promedioGeneral /= 6

# Impresión de resultados
print("Unidad 1\tUnidad 2\tUnidad 3\tUnidad 4\tUnidad 5\tPromedio")
for i in range(6):
    for j in range(5):
        # el "end" sirve para imprimir los resultados en una sola linea 
        print("{:.1f}\t\t".format(calificaciones[i][j]), end="")
    print(" {:.2f}".format(promediosMaterias[i]))

print("\nPromedio general: {:.2f}".format(promedioGeneral))

