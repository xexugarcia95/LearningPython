"""Escribir un programa que pregunte el nombre del usuario en la consola
y un número entero e imprima por pantalla en líneas distintas el nombre
del usuario tantas veces como el número introducido."""

mi_nombre = input("Introduce el nombre de usuario: ")
repeticion = int(input("Introduce el numero de repeticiones: "))

print((mi_nombre + "\n")*repeticion)

# Se puede hacer con bucle, pero como todavia no se ha llegado a esta parte
# se hace de una manera más simple
"""for i in range(repeticion):
    print(mi_nombre)"""
