"""Autor:  Orlando Urbano Trejo @Lando 
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcule el sueldo total de un empleado """
# Entrada de datos
horas = float(input("Horas Trabajadas: "))
sueldoHora = float(input("Sueldo por hora:"))
print("Sueldo total: ${:.2f}".format(horas * sueldoHora))
