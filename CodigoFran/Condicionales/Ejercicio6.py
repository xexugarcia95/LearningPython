"""Los alumnos de un curso se han dividido en dos grupos A y B
de acuerdo al sexo y el nombre. El grupo A esta formado por
las mujeres con un nombre anterior a la M y los hombres con
un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre
y sexo, y muestre por pantalla el grupo que le corresponde."""

nombre = input("Introduce tu nombre: ")
sexo = input("Introduce Sexo: ")
sexo_lower = sexo.lower()
if nombre < "M" and sexo_lower == "mujer":
    print("Perteneces al grupo A")
elif nombre > "N" and sexo_lower == "hombre":
    print("Perteneces al grupo A")
else:
    print("Pertenes al grupo B")
