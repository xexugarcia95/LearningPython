"""Escribir un programa que pregunte al usuario su nombre, edad, dirección
y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla
el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>."""

diccionario = {}
aux = input("Introduce un nombre: ")
diccionario["nombre"] = aux
aux = input("Introduce tu edad: ")
diccionario["edad"] = aux
aux = input("Introduce tu dirección: ")
diccionario["direccion"] = aux
aux = input("Teléfono: ")
diccionario["telefono"] = aux

print(str(diccionario.get("nombre")) + " tiene " + str(diccionario.get("edad"))
      + " años, vive en " + str(diccionario.get("direccion"))
      + " y su número de teléfono es "
      + str(diccionario.get("telefono")))
