"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes>
es el nombre del mes."""

diccionario = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo",
               6: "junio", 7: "julio", 8: "agosto", 9: "septiembre",
               10: "octubre", 11: "noviembre", 12: "diciembre"}

fecha = input("Introduce una fecha(dd/mm/aaaa): ")
fecha = fecha.split('/')
print(str(fecha[0]) + " de " + str(diccionario.get(int(fecha[1]))) + " de "
      + str(fecha[2]))
