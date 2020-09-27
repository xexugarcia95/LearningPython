"""Escribir un programa que pida al usuario una palabra
y muestre por pantalla el número de veces que contiene
cada vocal."""

palabra = input("Introduce una palabra: ")
letras = []
contador = [0, 0, 0, 0, 0]
for i in range(len(palabra)):
    letras.append(palabra[i])

print(letras[:])

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

print(f"El numero de a es: {contador[0]}")
print(f"El numero de e es: {contador[1]}")
print(f"El numero de i es: {contador[2]}")
print(f"El numero de o es: {contador[3]}")
print(f"El numero de u es: {contador[4]}")
