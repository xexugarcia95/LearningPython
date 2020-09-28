"""Escribir un programa que cree un diccionario simulando una cesta de la
compra. El programa debe preguntar el artículo y su precio y añadir el par
al diccionario, hasta que el usuario decida terminar. Después se debe mostrar
por pantalla la lista de la compra y el coste total, con el siguiente
formato"""

diccionario = {}

articulo = input("Introduce el artículo: ")
while articulo != '.':
    cantidad = float(input("Introduce el precio: "))
    diccionario[articulo] = cantidad
    articulo = input("Introduce el siguiente artículo: ")

print("Lista de la compra")
print("-------------------")
lista = list(diccionario.keys())
cont = 0
for i in range(len(lista)):
    print(lista[i] + "\t\t" + str(diccionario[lista[i]]))
    print("-------------------")
    cont += diccionario[lista[i]]
print("Total\t\t" + str(cont))
