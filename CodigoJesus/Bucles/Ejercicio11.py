"""Escribir un programa que pida al usuario una palabra y luego muestre
por pantalla una a una las letras de la palabra introducida empezando por
la última."""

pal = input("Introduce una palabra: ")

for i in range(len(pal)):
    print(pal[i])
