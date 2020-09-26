"""Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos
puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe
crear un diccionario con las palabras y sus traducciones. Después pedirá una
frase en español y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir."""

diccionario = {}
print("Formato de insercion: <palabra>:<traducción>")
palabra = input("Introduce: ")
while palabra !='.':
    palabra = palabra.split(":")
    diccionario[palabra[0]] = palabra[1]
    palabra = input("Introduce otra: ")
print("Pide palabras para obtener su traducción")
palabra = input("Introduce: ")
while palabra !='.':
    print(diccionario.get(palabra,"No existe esta palabra en el diccionario"))
    palabra = input("Introduce: ")
