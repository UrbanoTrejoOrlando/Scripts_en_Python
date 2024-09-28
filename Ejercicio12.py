"""Autor:  Orlando Urbano Trejo @Lando 
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula los intereses que tiene una persona con el banco"""

prestamo = 10000
interes = 0.27
# Entrada de datos
tiempo = int(input("Año en que se solicitó el préstamo: "))
tiempoTranscurrido = int(input("Año actual: "))

for i in range(tiempo, tiempoTranscurrido + 1):
    prestamo = prestamo + (prestamo * interes)
    print("El interés en el año {} es de: ${:.2f}".format(i, prestamo))   

