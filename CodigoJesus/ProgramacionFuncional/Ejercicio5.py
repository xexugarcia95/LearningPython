"""Escribir una función que reciba una frase y devuelva un diccionario
 con las palabras que contiene y su longitud."""


def apply_func(frase):
    lista = frase.split(' ')

    diccionario = map(len, lista)
    return dict(zip(lista, diccionario))


print(apply_func("hola amigo que tal estas"))
