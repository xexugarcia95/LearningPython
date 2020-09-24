"""Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior
a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
pantalla el grupo que le corresponde."""

nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo: ")

if sexo == "mujer":
    if nombre[0] <= 'm' or nombre[0] <= 'M':
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")
else:
    if nombre[0] >= 'n'or nombre[0] >= 'M':
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")
