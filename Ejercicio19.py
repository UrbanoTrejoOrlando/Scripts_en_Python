"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com 

Algoritmo que calcule el sueldo total de un empleado """

# Entrada de datos
nombre = input("Nombre: ")
salario = float(input("Salario: "))
print("Empleado:", nombre, "su salario es:", "{:.2f}".format(salario - (salario * 0.20)))
