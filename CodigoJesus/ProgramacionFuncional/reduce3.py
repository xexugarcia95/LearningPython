# Concatenar todos los elementos de la lista

from functools import reduce


lista = ['python', 'java', 'ruby', 'elixir']

resultado = reduce(
    lambda acumulador='',
    elemento='': acumulador+elemento,
    lista)

print(resultado)
