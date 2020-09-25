"""Escribir un programa que almacene en una lista los siguientes precios,
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el
mayor de los precios."""

tupla = (50,75,46,22,80,65,8)
mayor = 0
menor = 999999

for i in range(len(tupla)):
    if tupla[i] > mayor:
        mayor = tupla[i]
    if tupla[i] < menor:
        menor = tupla[i]

print("El mayor es " + str(mayor) + " y el menor es " + str(menor))
