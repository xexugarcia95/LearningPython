"""Escribir un programa que almacene el abecedario en una lista, elimine de la
lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla
la lista resultante."""

lista = []
lista2 = []
# chr() te convierte el numero en caracter de la tabla ascii correspondiente
for i in range(97,123,1):
    lista.append(chr(i))

for i in range(len(lista)):
    if (i+1)%3!=0:
        lista2.append(lista[i])
print("Lista antes: ")
print(lista[:])
print("Lista después: ")
print(lista2[:])
