"""Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión."""

inversion = float(input("Cantidad a invertir: "))
interes = float(input("Interes anual: "))
anio = int(input("Numero de años: "))

for i in range(1, anio+1, 1):
    print(str(round(inversion*(interes/100+1)**i, 2)))
