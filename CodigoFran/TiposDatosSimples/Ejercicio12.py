"""Imagina que acabas de abrir una nueva cuenta de
ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran
hasta finales de año, se te añaden al balance final
de tu cuenta de ahorros. Escribir un programa que
comience leyendo la cantidad de dinero depositada en
la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla
la cantidad de ahorros tras el primer, segundo y
tercer años. Redondear cada cantidad a dos decimales."""

dinero = input("Cuanto dinero tiene depositado en la cuenta: ")
interes = 0.04
suma = float(dinero)

for i in range(3):
    ganancia = int(suma) * float(interes)
    suma += ganancia
    round(suma, 2)
    print(f"El dinero tras el año {i+1} es {suma}")
