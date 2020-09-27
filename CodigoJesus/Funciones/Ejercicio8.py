"""Escribir una función que reciba una muestra de números en una lista y
devuelva un diccionario con su media, varianza y desviación típica."""

def medVarDes(list):
    media = 0
    var = 0
    desv = 0
    diccionario = {}
    for i in range(len(list)):
        media+=list[i]
    media/=len(list)
    diccionario["media"] = round(media,2)
    for i in range(len(list)):
        var+=(list[i]-media)**2
    var/=len(list)
    diccionario["varianza"] = round(var,2)
    desv = var**(1/2)
    diccionario["Desviacion tipica"] = round(desv,2)
    return diccionario

lista = [4,6,10,5,8,3]
print(str(medVarDes(lista)))
