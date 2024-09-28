""""Autor: Orlando Urbano Trejo @Lando 
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula la cantidad de euros a monedas y viceversa """

print("-------- MENU DE CONVERSIONES --------\n1) Euros\n2) Dolares")i
# Entrada de datos
opcion = int(input("Elige una opción: "))
# Condiciones
if opcion == 1:
    dinero = int(input("Dinero: "))
    print("Dinero: {:.2f} euros".format(dinero / 0.053))
elif opcion == 2:
    dinero = int(input("Dinero: "))
    print("Dinero: {:.2f} dólares".format(dinero / 16.89))
else:
    print("Opción no válida")



