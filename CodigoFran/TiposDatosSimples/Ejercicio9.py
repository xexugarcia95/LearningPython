"""Escribir un programa que pida al usuario dos números enteros
y muestre por pantalla la <n> entre <m> da un cociente <c> y
un resto <r> donde <n> y <m> son los números introducidos por
el usuario, y <c> y <r> son el cociente y el resto de la división
entera respectivamente."""

numerador = input("Introduce el numerador: ")
denominador = input("Introduzca el denominador: ")

cociente = int(numerador)//int(denominador)
resto = int(numerador) % int(denominador)

print(f"{numerador} entre {denominador} da un cociente de {cociente} y un resto de {resto}")
