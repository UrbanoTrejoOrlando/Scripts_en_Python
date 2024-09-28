"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com 

Algoritmo que calcula las comisiones de un empleado dependiendo de las ventas realizadas """

# Entrada de datos
sueldo = float(input("Sueldo fijo: "))
ventas = int(input("Ventas realizadas: "))
comision = 0
for i in range(ventas):
    precioVenta = float(input("Precio de la venta {}: ".format(i+1)))
    comision += precioVenta * 0.10
total = comision + sueldo
print("Comisión: ${:.2f}".format(comision))
print("Sueldo: ${:.2f}".format(total))

