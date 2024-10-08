"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  18-08-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Crear un programa que realice un menu de conversion de unidades."""

General = [
     "---CONVERSION DE UNIDADES----",
     "0) Longitud",
     "1) Masa",
     "2) Tiempo",
     "3) Volumen",
     "4) Tamaño de Datos",
     "5) Velocidad",
     "&) Temperatura"]

Menu = [
    ["m","cm","km","mm","mi","yd","ft","in"],
    ["kg","to","g","st","lb","oz"],
    ["m","ml","s","hr","d"],
    ["l","ml","gal","ozl","m3","ft3","in3"],
    ["bit", "kl","B","kb"],
    ["mi/h","ft/s","m/s","km/h","kn"],
    ["°C","°F","K"]]

Operaciones = [
    [1, 100, 0.001, 1000, 0.000621371, 1.09361, 3.28084, 39.3701],
    [1,0.001, 1000, 0.157473, 2.20462, 35.274],
    [1, 6000, 60, 0.0166667, 0.000694444],
    [1, 1000, 0.219969, 35.1951, 0.001, 0.0353147, 61.0237],
    [1,0.001,0.125,0.000125],
    [1,1.46667,0.44704,1.60934,0.868976],
    [1,1.8,1]]

for i in range(7):
    print(General[i])

Opcion = int(input("Elige una opcion: "))
if Opcion >= 0 and Opcion <= 6:
    for j in range(len(Menu[Opcion])):
        print(f"{j}) {Menu[Opcion][j]}")

UnidadEntrada = int(input("Elige la unidad de entrada: " ))
UnidadDestino = int(input("Elige la unidad de destino: " ))
Valor = float(input("Introduce e valor a convertir: " ))
Resultado = 0
Resultado = Valor * (Operaciones[Opcion][UnidadDestino] / Operaciones[Opcion][UnidadEntrada])
print(Valor , Menu[Opcion][UnidadEntrada] , " = ", Resultado, Menu[Opcion][UnidadDestino])
