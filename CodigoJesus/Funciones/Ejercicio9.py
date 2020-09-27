"""Escribir una función que calcule el máximo común divisor de dos números y
otra que calcule el mínimo común múltiplo."""

def divisores(n):
    lista = []
    for i in range(1,n,1):
        if n%i==0:
            lista.append(i)
    return lista

def multiplos(n):
    lista = []
    for i in range(1,n+1,1):
        if n%i==0:
            lista.append(i)
    return lista

def mcd(n1,n2):
    lista1 = divisores(n1)
    lista2 = divisores(n2)
    maximo = 1
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j] and lista2[j]>maximo:
                maximo = lista2[j]
    return maximo

def mcm(n1,n2):
    lista1 = multiplos(n1)
    lista2 = multiplos(n2)
    min = 999999
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j]:
                min = lista2[j]
    return min

print(" MCD --> " + str(mcd(15,30)) + " MCM --> " + str(mcm(15,30)))
