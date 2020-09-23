"""Escribir un programa que pida al usuario un
número entero y muestre por pantalla un triángulo
rectángulo como el de más abajo, de altura el
número introducido."""

numero = int(input("Introduce un numero entero y positivo: "))

if numero > 0:
    for i in range(numero):
        for j in range(numero):
            if j <= i:
                print("* ", end="")
            if j == i:
                print("")
else:
    print("Numero introducido incorrecto.")
