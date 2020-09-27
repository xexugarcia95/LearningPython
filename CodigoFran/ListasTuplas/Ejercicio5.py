"""Escribir un programa que almacene en una lista los números
del 1 al 10 y los muestre por pantalla en orden inverso
separados por comas."""

lista = []

for i in range(10):
    lista.append(i+1)

print(lista[:])


"""Con esto lo que hacemos es invertir la lista, lo que
tenemos que tener en cuenta es que la lista es modificada"""
lista = lista[::-1]

print(lista[:])
