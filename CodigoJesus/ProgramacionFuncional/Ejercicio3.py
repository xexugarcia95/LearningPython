"""Escribir una función que reciba otra función y una lista, y devuelva otra
lista con el resultado de aplicar la función dada a cada uno de los
elementos de la lista."""


def apply_function(function, list):
    lista = []
    for i in list:
        lista.append(function(i))

    return lista


def raiz(n):
    return int(n**0.5)


print(apply_function(raiz, [1, 4, 9, 16, 25, 36, 49]))
