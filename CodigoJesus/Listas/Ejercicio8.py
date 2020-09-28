"""Escribir un programa que pida al usuario una palabra y muestre por
pantalla si es un palíndromo."""

palabra = input("Introduce una palabra: ")
palabra2 = ""
for i in range(len(palabra)-1, -1, -1):
    palabra2 += palabra[i]

print("El resultado de mostrarlo al revés es: " + palabra2)
if palabra == palabra2:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
