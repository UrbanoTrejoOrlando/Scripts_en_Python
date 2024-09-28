"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  17-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que almacena calificaciones de alumnos y calcula su promedio """
calificacion = [0] * 5
# Entrada de datos
materia = input("Materia: ")

for i in range(1, 6):
    calificacion[i - 1] = int(input(f"Calificacion en la Unidad {i}: "))
    suma += calificacion[i - 1]

print(f"Asignatura: {materia}")
print("Unidad 1\tUnidad 2\tUnidad 3\tUnidad 4\tUnidad 5\tPromedio")

for i in range(5):
    print(f"{calificacion[i]:8}\t", end="")
# Operaciones 
promedio = suma / 5
# Impresion de resultado
print(f"{promedio:.2f}")

