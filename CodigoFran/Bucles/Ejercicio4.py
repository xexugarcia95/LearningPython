"""Escribir un programa que pida al usuario un número
entero positivo y muestre por pantalla la cuenta atrás
desde ese número hasta cero separados por comas."""

numero = int(input("Introduce un numero positivo: "))

if numero > 0:
    for i in range(numero+1):
        cuenta = numero - i
        print(cuenta)
