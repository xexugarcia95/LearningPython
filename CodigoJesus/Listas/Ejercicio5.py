"""Escribir un programa que almacene en una lista los números del 1 al 10 y
los muestre por pantalla en orden inverso separados por comas."""

lista = []

for i in range(1,11,1):
    lista.append(i)

for i in range(len(lista)-1,-1,-1):
    print(lista[i])
