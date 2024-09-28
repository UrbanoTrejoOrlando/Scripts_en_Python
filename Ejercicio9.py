"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  13-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo para determinar el sueldo semanal de N trabajdores y aplicar descuentos dependiendo de las horas se aplicara un descuento """

# Datos de entrada
trabajadores = int(input("Número de trabajadores: "))
for i in range(trabajadores):
    nombres = input(f"Nombre del trabajador {i+1}: ")
    horasTrabajadas = float(input("Horas trabajadas: "))
    sueldoHora = float(input("Sueldo por hora: "))

    salario = horasTrabajadas * sueldoHora
    nuevoSalario = 0
    # Condiciones
    if salario >= 0 and salario <= 150:
        nuevoSalario = salario * 0.95
    elif salario > 150 and salario <= 300:
        nuevoSalario = salario * 0.93
    elif Salario > 300 and Salario <= 450:
        nuevoSalario = salario * 0.91
    
    total = salario - nuevoSalario
    print(f"Trabajador: {nombres}")
    print(f"Salario final: {total:.2f}")

