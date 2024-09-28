"""Autor: Orlando Urbano Trejo @Lando
   Fecha: 13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula el presupuesto anual en tres areas de un hospital """

# Entrada de datos 
presupuesto = int(input("Presupuesto anual: "))
# Impresion de resultados
print("Presupuesto Urgencias: ${:.2f}".format(presupuesto * 0.37))
print("Presupuesto Pediatria: ${:.2f}".format(presupuesto * 0.42))
print("Presupuesto Traumatologia: ${:.2f}".format(presupuesto * 0.21))


