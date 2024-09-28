"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo para calcular el descuento de un medicamento """
# Entrada de datos
nombre = input("Nombre: ")
precio = float(input("Precio del medicamento: "))
# Impresion de resultados
print("Cliente:", nombre, "el total a pagar: $", "{:.2f}".format(precio - (precio * 0.35)))

