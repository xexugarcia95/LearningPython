"""Escribir una función que calcule el módulo de un vector."""

from functools import reduce


def cuadrado(x, y):
    return x+y**2


def module(tupla):
    return reduce(cuadrado, tupla, 0)**0.5


print(module((2, 3)))
print(module((4, 3)))
