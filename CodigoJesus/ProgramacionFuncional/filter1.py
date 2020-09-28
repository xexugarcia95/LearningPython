# filter(funcion a aplicar, objeto iterable)
# Obtener los elementos mayores de 5 de la tupla


def mayor_a_cinco(elemento):
    return elemento > 5


tupla = (2, 3, 8, 1, 5, 6, 9, 4, 1, 7, 5, 4, 10)


resultado = tuple(filter(mayor_a_cinco, tupla))

print(resultado)
