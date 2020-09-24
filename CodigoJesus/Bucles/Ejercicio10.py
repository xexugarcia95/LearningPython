"""Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es un número primo o no."""

num = int(input("Introduce un numero entero: "))
contador = 0

for i in range(1,num+1,1):
    if num%i==0:
        contador+=1

if contador==2:
    print("Numero primo")
else:
    print("Numero no primo")
