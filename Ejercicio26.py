"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  17-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula la calficacion de N alumnos y calcula el promedio general """
suma = 0
promedio = 0
# Entrada de datos
alumno = int(input("Cuantos alumnos hay en el salon: "))
for i in range(alumno):
    edad = int(input(f"Edad del alumno {i+1}: "))
    suma += edad
# Operaciones
promedio = suma / alumno
print("El promedio de las edades de los alumnos es: ",promedio)
