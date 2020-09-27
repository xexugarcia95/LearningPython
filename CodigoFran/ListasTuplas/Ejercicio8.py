"""Escribir un programa que pida al usuario una
palabra y muestre por pantalla si es un palíndromo."""


palabra = input("Introduzca una palabra: ")

letras = []

for i in range(len(palabra)):
    letras.append(palabra[i])

inversion = letras[::-1]

if inversion == letras:
    print(f"{palabra} ES una palabra palindroma")
else:
    print(f"{palabra} NO ES una palabra palindroma")
