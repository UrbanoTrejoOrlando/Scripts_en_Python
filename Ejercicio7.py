"""Autor:  Orlando Urbano Trejo @Lando 
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo para leer calificaciones de N alumnos y calcular el numero de aprobados y reprobados"""
# Datos de entrada
alumnos = int(input("Cantidad de alumnos: "))
aprobados = 0
reprobados = 0

for i in range(alumnos):
    # Recabar calificacion de alumnos
    calificacion = float(input(f"Calificación del alumno {i+1} (1-100): "))
    # Condiciones
    if calificacion > 70:
        print("APROBADO")
        aprobados += 1
    else:
        print("REPROBADO")
        reprobados += 1
print(f"Número de alumnos aprobados: {aprobados}")
print(f"Número de alumnos reprobados: {reprobados}")

