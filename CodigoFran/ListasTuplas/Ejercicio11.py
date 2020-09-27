"""Escribir un programa que almacene los vectores
(1,2,3) y (-1,0,2) en dos listas y muestre por
pantalla su producto escalar."""

vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)
lista = []
for i in range(len(vector1)):
    lista.append(vector1[i]*vector2[i])
suma = 0
for i in range(len(lista)):
    suma += lista[i]
print(lista[:])
print(f"El producto escalar es: {suma}")
