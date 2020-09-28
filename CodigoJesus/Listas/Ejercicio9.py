"""Escribir un programa que pida al usuario una palabra y muestre por pantalla
el número de veces que contiene cada vocal."""

palabra = input("Introduce una palabra/frase: ")
contador = [0, 0, 0, 0, 0]

for i in range(len(palabra)):
    if palabra[i] == 'a':
        contador[0] += 1
    if palabra[i] == 'e':
        contador[1] += 1
    if palabra[i] == 'i':
        contador[2] += 1
    if palabra[i] == 'o':
        contador[3] += 1
    if palabra[i] == 'u':
        contador[4] += 1

print(contador)
