"""Autor:  Orlando Urbano Trejo @Lando 
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcule el total de una caja registradora """

dinero = [1000, 500, 200, 100, 50, 20, 5, 2, 1, 0.50, 0.20, 0.10]
resultado = 0
for i in range(12):
    # Datos de entrada
    print("Cantidad de dinero que tiene: %.2f pesos" % dinero[i])
    convertidor = int(input())
    resultado += (convertidor * dinero[i])
    print("Total almacenado: $",resultado)



