"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo para calcular el tiempo que tarda una persona en llegar a un lugar """

# Datos de entrada 
distancia = float(input("Distancia (en kilómetros): "))
velocidad = float(input("Velocidad (en kilómetros por hora): "))
# Impresion de resultadosi
print(f"El tiempo total de viaje es de {(distancia * velocidad) / 60} horas.")
