"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  17-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo para calcular el factorial de un numero. """

resultado = 1
# Entrada de datos
numero = int(input("Ingresa un numero: "))
for i in range(1, numero + 1):
    resultado *= i
    print("Resultado: ",resultado)
   

