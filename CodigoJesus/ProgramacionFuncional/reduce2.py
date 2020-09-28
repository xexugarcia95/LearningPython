from functools import reduce

lista = [1, 2, 3, 4]

resultado = reduce(lambda acumulador=0, elemento=0: acumulador+elemento, lista)

print(resultado)
