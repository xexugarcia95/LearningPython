"""Una panadería vende barras de pan a 3.49€ cada una.
El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de
barras vendidas que no son del día. Después el programa
debe mostrar el precio habitual de una barra de pan, el
descuento que se le hace por no ser fresca y el coste final
total."""

barras = input("Introduce el numero de barras vendidas que no son del dia: ")
descuento = 0.6
frescas = 3.49

x = descuento * frescas
p = frescas - x
total = int(barras)*p
total = round(total, 2)

print(f"El precio habitual de una barra de pan es {frescas} euros")
print(f"El descuento que se le aplica es {descuento*100}%")
print(f"El precio total de las barras no frescas es: {total} euros")
