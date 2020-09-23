"""Escribir un programa que pida al usuario un número
entero y muestre por pantalla si es un número primo o no."""

numero = int(input("Introduce un numero positivo: "))
contador = 0

if numero > 0:
    for i in range(numero):
        if numero % (i+1) == 0:
            contador += 1

    if contador == 2:
        print("El numero es PRIMO")
    else:
        print("El numero NO ES PRIMO")
