"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula el precio total del boleto de una persona, ingresando los datos por teclado"""
# Datos de entrada
precioKilometro = float(input("Precio por kilometro: "))
distancia = float(input("Kilometros a recorrer: "))
print("Precio boleto: $",(precioKilometro * distancia))
