"""Escribir un programa que almacene el diccionario con los créditos de las
asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas
del curso, y <créditos> son sus créditos. Al final debe mostrar también el
número total de créditos del curso."""

diccionario = {"matematicas": 6, "fisica": 4, "quimica": 5}
lista = list(diccionario)

for key in diccionario.keys():
    print(str(key) + " tiene " + str(diccionario.get(key)) + " creditos")

cont = 0
for value in diccionario.values():
    cont += value

print("El total de créditos es " + str(cont))
