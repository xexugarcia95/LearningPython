"""Escribir un programa que pregunte al usuario una cantidad
a invertir, el interés anual y el número de años, y muestre
por pantalla el capital obtenido en la inversión cada año
que dura la inversión."""

inversion = int(input("Introducir la inversion: "))
interes = float(input("Introduce el interes anual: "))
años = int(input("Introduce la cantidad de años: "))

for i in range(años):
    print(f"Año {i+1}:")
    ganancia = inversion * interes
    inversion += ganancia
    round(inversion, 2)
    print(f"Cantidad de {inversion}€")
