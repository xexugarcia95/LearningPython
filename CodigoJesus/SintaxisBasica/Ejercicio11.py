"""Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión."""

invertir = int(input("Cantidad a invertir: "))
interes = float(input("Interes anual: "))
num = int(input("Numero de años: "))
capitalFinal = round(invertir*(interes/100+1)**num,2)

print("Capital obtenido: " + str(capitalFinal))
