"""Escribir un programa que lea un entero positivo, n,
introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta n.
La suma de los n  primeros enteros positivos puede ser
calculada de la siguiente forma"""

numero = input("Introduce un numero: ")

suma = (int(numero)*(int(numero)+1))/2

print(f"La suma de todos los digitos es {int(suma)}")
