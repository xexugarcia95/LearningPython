"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al
usuario la nota que ha sacado en cada asignatura, y después las muestre por
pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura>
 es cada una des las asignaturas de la lista y <nota> cada una de las
 correspondientes notas introducidas por el usuario."""

lista = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
lista2 = []

for i in range(len(lista)):
    lista2.append(int(input("Qué nota has sacado en " + lista[i] + "?: ")))

for i in range(len(lista)):
    print("En " + lista[i] + " he sacado un " + str(lista2[i]))
