"""Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña e imprima por
pantalla si la contraseña introducida por el usuario coincide con
la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

contraseña = input("Introduce la contraseña: ")
contraseña_lower = contraseña.lower()
comprobar = "contraseña"
print(f"{contraseña_lower}")

if contraseña_lower == comprobar:
    print("La contraseña introducida es la correcta")
else:
    print("La contraseña introducida no es correcta")
