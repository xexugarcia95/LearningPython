"""Escribir una función reciba un diccionario con las asignaturas y las
notas de un alumno y devuelva otro diccionario con las asignaturas en
mayúsculas y las calificaciones correspondientes a las notas aprobadas."""


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


def aprobado(n):
    return n[1] >= 5


def apply_function(diccionario):
    aprobados = dict(filter(aprobado, diccionario.items()))
    asignatura = map(mayus, aprobados.keys())
    notas = map(nota, aprobados.values())
    return dict(zip(asignatura, notas))


print(apply_function({"mates": 3, "lengua": 8, "fisica": 5,
                      "sociales": 10, "gimnasia": 7}))
