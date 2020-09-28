"""Escribir una función reciba una lista de notas y devuelva la lista de
calificaciones correspondientes a esas notas."""


def nota(n):
    if n < 5:
        return "SUSPENSO"
    elif n >= 5 and n < 7:
        return "APROBADO"
    elif n >= 7 and n < 9:
        return "NOTABLE"
    elif n >= 9:
        return "SOBRESALIENTE"


def notas(lista):
    resultado = map(nota, lista)
    return dict(zip(lista, resultado))


print(notas([5, 4, 10, 6, 9, 7, 2, 6, 4, 8]))
