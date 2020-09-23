"""Escribir un programa en el que se pregunte
al usuario por una frase y una letra, y muestre
por pantalla el número de veces que aparece la
letra en la frase."""

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")


contador = 0

for i in range(len(frase)):
    if frase[i] == letra:
        contador += 1

print(f"La frase tiene la letra {letra} {contador} veces")
