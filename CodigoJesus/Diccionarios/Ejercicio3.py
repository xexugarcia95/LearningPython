"""Escribir un programa que guarde en un diccionario los precios de las frutas
de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre
por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en
el diccionario debe mostrar un mensaje informando de ello."""

diccionario = {"platano":1.35,"manzana":0.80,"pera":0.85,"naranja":0.70}

fruta = input("Elige una fruta: ")
kil = int(input("Número de kilos: "))
val = diccionario.get(fruta,0)
if val != 0:
    print("Precio: " + str(kil*float(diccionario.get(fruta))))
else:
    print("No existe esta fruta")
