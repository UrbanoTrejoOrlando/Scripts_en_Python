"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  18-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que multiplique dos arreglos"""

primero = []
segundo = []
multiplicacion = []
for i in range(5):
    # Entrada de datos
    primero.append(int(input("Valor " + str(i+1) + ": ")))
print()
for i in range(4, -1, -1):
    suma = i + 2
    segundo.insert(0, int(input("Valor " + str(suma-1) + ": ")))

for i in range(5):
    # Multiplicacion de arreglos
    multiplicacion.append(primero[i] * segundo[i])

print("Resultado:", multiplicacion)

