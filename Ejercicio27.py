"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  17-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula el descuento de 3 tipos de vestidos """

print("----VESTIDOS----\n1) Grande $500\n2) Mediana $400\n3) Chica $300")
# Entrada de datos
vestido = int(input("Elige la marca que deseas comprar (1-3): "))
# Condiciones
if vestido == 1:
    cantidad = int(input("Numero de vestidos que deseas comprar: "))
    total = cantidad  * 500
elif vestido == 2:
    cantidad = int(input("Numero de vestidos que deseas comprar: "))  
    total = cantidad  * 400
elif vestido == 3:
    cantidad = int(input("Numero de vestidos que deseas comprar: "))
    total = cantidad  * 300
else:
    print("Opcion no valida")

print("Monto total de la venta: $",total)


