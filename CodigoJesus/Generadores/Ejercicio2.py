"""Generador que devuelve ciudades"""


def devuelveCiudades(*ciudades):
    for i in ciudades:
        yield i


def devuelveCiudades2(*ciudades):
    for i in ciudades:
        yield from i


misCiudades = devuelveCiudades("Madrid", "Barcelona", "Sevilla")
print(next(misCiudades))
print(next(misCiudades))
print(next(misCiudades))
misCiudades2 = devuelveCiudades2("Madrid", "Barcelona", "Sevilla")
print(next(misCiudades2))
print(next(misCiudades2))
