"""Escribir un programa que pregunte el nombre del
usuario en la consola y después de que el usuario
lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n>
es el número de letras que tienen el nombre."""

nombre = input("Cual es tu nombre?: ")
print(f"El nombre es {nombre}, y tiene {len(nombre)} letras")


"""len() es el equivalente en python al a.length() en c++
para determinar la longitud de una cadena de caracteres"""
