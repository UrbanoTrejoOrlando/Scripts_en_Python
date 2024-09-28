"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula la cantidad de ventas que realiza un vendedor y de acuerdo a esas ventas, realizar un descuento """

ventas = 0
totalFinal = 0
total = 0
cantidad = []

# Entrada de datos
ventas = int(input("Numero de ventas: "))
for i in range(ventas):
    venta = float(input("Precio de la venta {}: ".format(i + 1)))
    cantidad.append(venta)
    totalFinal += cantidad[i]

    # Condiciones
    if cantidad[i] < 1000:
        total += cantidad[i]
    elif cantidad[i] > 1000 and cantidad[i] < 2000:
        total += cantidad[i]

# Impresion de resultados
print("Total final:", totalFinal)

