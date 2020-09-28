"""Generador de pares con un límite"""

def generadorPares(limite):
    cont = 1
    while cont<limite:
        yield cont*2
        cont+=1

pares = generadorPares(10)
for i in pares:
    print(i)
