"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo para determinar el pago que debe realizar una persona por el consumo de agua """

# Datos de entrada
precioMetros = int(input("Ingresa el precio por metro: "))
metros = int(input("Metros consumidos: "))
print("Pago: ${:.2f}".format(precioMetros * metros))

