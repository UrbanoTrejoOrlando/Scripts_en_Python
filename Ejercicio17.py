"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula la cantidad total de dinero que tienes """

cajero = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50]
cantidad = 0
for i in range(len(cajero)):
    # Entrada de datoa
    dinero = int(input("Cantidad de {:.2f} que tiene: ".format(cajero[i])))
    cantidad += dinero * cajero[i]
    print("Total: ${:.2f}".format(cantidad))

