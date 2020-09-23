"""Escribir un programa que pida al usuario un número
entero positivo y muestre por pantalla todos los
números impares desde 1 hasta ese número separados por comas."""

numero = input("Introduce un numero positivo: ")

numero = int(numero)

print("Los numeros impares son: ")
if numero > 0:
    for i in range(numero):
        if i % 2 != 0:
            print(i)
