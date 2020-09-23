"""Escribir un programa que pida al usuario un
número entero y muestre por pantalla si es
par o impar."""

numero = input("Introduce un numero: ")

if int(numero) % 2 == 0:
    print("El numero introducido es PAR")
else:
    print("El numero introducido es IMPAR")
