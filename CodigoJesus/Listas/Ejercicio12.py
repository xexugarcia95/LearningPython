"""Escribir un programa que almacene las matrices en una lista y muestre
por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas,
representando cada vector fila en una lista."""

A = ((1, 2, 3), (4, 5, 6))
B = ((-1, 0), (0, 1), (1, 1))
resultado = [[0, 0], [0, 0]]


for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            resultado[i][j] += A[i][k]*B[k][j]

for i in range(len(resultado)):
    resultado[i] = tuple(resultado[i])
resultado = tuple(resultado)

for i in range(len(resultado)):
    print(resultado[i])
