"""Escribir un programa que almacene la
cadena de caracteres contraseña en una
variable, pregunte al usuario por la
contraseña hasta que introduzca la contraseña
correcta."""

contraseña = input("Introduzca la contraseña: ")
seguridad = "calcetines"
while contraseña != seguridad:
    contraseña = input("Introduzca la contraseña: ")

print("Exito, contraseña correcta")
