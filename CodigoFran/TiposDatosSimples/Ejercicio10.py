"""Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión."""

cantidad = input("Introduce la cantidad que desea invertir en euros: ")
interes = input("Introduce cual es el interes anual: ")
años = input("Introduce el numero de años")

ganancia = float(cantidad) * float(interes) * int(años)
resultado = float(cantidad) + float(ganancia)

print(f"El capital obtenido en la inversion asciende a {resultado} euros")
