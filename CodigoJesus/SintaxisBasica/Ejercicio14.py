"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día
tiene un descuento del 60%. Escribir un programa que comience leyendo el número
de barras vendidas que no son del día. Después el programa debe mostrar el precio
habitual de una barra de pan, el descuento que se le hace por no ser fresca y
el coste final total."""

barras = int(input("Numero de barras vendidas: "))
descuento = round(float(3.49*0.6),2)
print("Precio habitual: 3.49")
print("Descuento por no ser del día: " + str(descuento))
print("Coste total: " + str(barras*descuento))
