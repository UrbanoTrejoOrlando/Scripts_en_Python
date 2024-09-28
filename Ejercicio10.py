"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que calcula el saldo de sus clientes para no generar intereses y dependiendo del año aplicar descuentos """

# Datos de entrada
clientes = int(input("Número de clientes: "))
for i in range(clientes):
    # Almacenar datos de entrada
    nombre = input("Nombre del cliente: ")
    saldoAnterior = float(input("Saldo anterior: "))
    deposito = float(input("Último depósito: "))
    montoCompras = float(input("Monto por ventas: "))
    saldoActual = float(input("Saldo actual: "))
    # Operaciones
    pagoActual = (saldoActual * 0.12) + 200
    saldoMinimo = saldoActual * 0.15
    pagoInteres = saldoActual * 0.85
    # Impresion de resultados
    print("Tu saldo actual, {} es de {:.2f} pesos".format(nombre, pagoActual))
    print("Tu pago mínimo, {} es de {:.2f} pesos".format(nombre, saldoMinimo))
    print("El pago para no generar intereses, {} es de {:.2f} pesos".format(nombre, pagoInteres))

