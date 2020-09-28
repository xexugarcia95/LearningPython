"""Escribir una función que reciba otra función booleana y una lista,
 y devuelva otra lista con los elementos de la lista que devuelvan
  True al aplicarles la función booleana."""


def apply_funcion(bool_func, list):
    lista = []
    for i in list:
        if bool_func(i) is True:
            lista.append(i)

    return lista


def par(n):
    return n % 2 == 0


print(apply_funcion(par, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
