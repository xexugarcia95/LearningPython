"""Escribir una función que reciba una muestra de números en una lista y
devuelva su media."""


def media(lista):
    cont = 0
    for i in range(len(lista)):
        cont += lista[i]
    cont /= len(lista)
    return cont


list = [1, 2, 3, 4, 5]
print(str(media(list)))
