"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  18-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcule el descuento de una urna dependiendo del tipo de pelota que saque """

print("-----CAFETERIA TESJI-----\n1) Pelota Verde\n2) Pelota Roja\n3) Pelota Amarilla")
# Entrada de datos
pelota = int(input("Elige una opcion: "))
# Condiciones
if pelota == 1:
    print("Descuento 10%")
    compra = float(input("Total de tu compra: "))
    resultado = compra - (compra * 0.10)
    print(f"Monto total: ${resultado:.2f}")
elif pelota == 2:
    print("Descuento 5%")
    compra = float(input("Total de tu compra: "))
    resultado = compra - (compra * 0.05)
    print(f"Monto total: ${resultado:.2f}")
elif pelota == 3:
    print("Descuento 15%")
    compra = float(input("Total de tu compra: "))
    resultado = compra - (compra * 0.15)
    print(f"Monto total: ${esultado:.2f}")
else:
    print("Opcion no valida")

