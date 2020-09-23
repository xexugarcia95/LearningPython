"""Escribir un programa que lea un entero positivo,n, introducido por el usuario
y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
suma = n(n+1)/2"""
entero = int(input("Introduce un numero entero positivo: "))
suma = entero*(entero+1)//2
print("La suma de los " + str(entero) + " primeros enteros es: " + str(suma))
