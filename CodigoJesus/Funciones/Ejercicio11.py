"""Escribir un programa que reciba una cadena de caracteres y devuelva un
diccionario con cada palabra que contiene y su frecuencia. Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla
con la palabra más repetida y su frecuencia."""

def funcion(cadena):
    lista = cadena.split(" ")
    diccionario = {}
    for i in range(len(lista)):

        if lista[i] in diccionario:
            val = int(diccionario[lista[i]])
            val+=1
            diccionario[lista[i]] = val
        else:
            diccionario[lista[i]] = 1

    return diccionario

def moda(diccionario):
    key = ""
    val = 0
    caracteres = diccionario.items()
    for nombre,freq in caracteres:
        if freq>val:
            key = nombre
            val = freq
    tupla = (key,val)
    return tupla

diccionario = funcion("hola hola hola no estas sola caracola no eh")
print(moda(diccionario))
