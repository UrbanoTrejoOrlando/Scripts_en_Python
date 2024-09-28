"""Autor:  Orlando Urbano Trejo @Lando
   Fecha:  17-07-2023
   Correo: orlandourbanotrejo@gmail.com

Algoritmo que imprima un arbol de navidad """

# Datos de entrada
altura = int(input("Altura del árbol: "))

# Imprimir la parte superior del árbol
for i in range(1, altura + 1):
    espacios = altura - i

    # Imprimir espacios en blanco
    for j in range(espacios):
        print(" ", end="")

    # Imprimir asteriscos
    for j in range(2 * i - 1):
        print("*", end="")

    print()

tronco = altura - 1
# Imprimir el tronco del árbol
for i in range(2):
    for j in range(tronco):
        print(" ", end="")

    print("**")

