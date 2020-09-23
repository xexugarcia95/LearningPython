"""Escribir un programa que pregunte el nombre del usuario en
la consola y un número entero e imprima por pantalla en
líneas distintas el nombre del usuario tantas veces como
el número introducido."""

nombre = input("Cual es tu Nombre?: ")
numero = input("Introduce un numero: ")

"""el input me guarda como un string lo que meto
por eso hacemos una conversion a entero"""
for i in range(int(numero)):
    print(nombre)
