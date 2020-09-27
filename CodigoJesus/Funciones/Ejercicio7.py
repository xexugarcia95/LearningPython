"""Escribir una función que reciba una muestra de números en una lista y
devuelva otra lista con sus cuadrados."""

def cuadrados(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]**2
    return lista

lista = [1,2,3,4,5]

print(str(cuadrados(lista)))
