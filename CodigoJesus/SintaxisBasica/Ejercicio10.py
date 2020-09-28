"""Escribir un programa que pida al usuario dos números enteros y muestre por
pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m>
son los números introducidos por el usuario, y <c> y <r> son el cociente y
el resto de la división entera respectivamente."""

number1 = int(input("Introduce el primer numero: "))
number2 = int(input("Intrdoduce el segundo numero: "))

print("La " + str(number1) + " entre " + str(number2) + " da un cociente "
      + str(number1//number2)
      + " y un resto " + str(number1 % number2))
