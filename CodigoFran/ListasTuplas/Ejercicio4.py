"""Escribir un programa que pregunte al usuario los números ganadores
de la lotería primitiva, los almacene en una lista y los muestre
por pantalla ordenados de menor a mayor."""

lista = []

numero = 0

while numero != ".":

    numero = input("Introduzca un numero ganador: ")
    if numero != ".":
        lista.append(int(numero))


lista.sort()
print(lista[:])
