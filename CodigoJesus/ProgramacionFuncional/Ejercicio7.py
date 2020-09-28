"""Escribir una función reciba un diccionario con las asignaturas y
las notas de un alumno y devuelva otro diccionario con las asignaturas
en mayúsculas y las calificaciones correspondientes a las notas."""


def nota(n):
    if n < 5:
        return "SUSPENSO"
    elif n >= 5 and n < 7:
        return "APROBADO"
    elif n >= 7 and n < 9:
        return "NOTABLE"
    elif n >= 9:
        return "SOBRESALIENTE"


def mayus(cad):
    return cad.upper()


def apply_function(diccionario):
    nombres = diccionario.keys()
    nombres = map(mayus, nombres)
    notas = diccionario.values()
    notas = map(nota, notas)

    return dict(zip(nombres, notas))


print(apply_function({"mates": 3, "lengua": 8, "fisica": 5,
                      "sociales": 10, "gimnasia": 7}))
