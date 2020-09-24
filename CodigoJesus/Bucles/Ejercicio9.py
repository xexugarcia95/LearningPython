"""Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña hasta que introduzca
la contraseña correcta."""

cadena = "contraseña"
val = input("Introduce contraseña: ")
while val!= cadena:
    val=input("Incorrecta, introduce otra contraseña: ")

print("Contraseña correcta")
