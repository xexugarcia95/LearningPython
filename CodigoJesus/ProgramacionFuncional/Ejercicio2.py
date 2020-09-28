"""Escribir una función que simule una calculadora científica que permita
calcular el seno, coseno, tangente, exponencial y logaritmo neperiano.
La función preguntará al usuario el valor y la función a aplicar,
y mostrará por pantalla una tabla con los enteros de 1 al valor introducido
y el resultado de aplicar la función a esos enteros."""

from math import sin, cos, tan, exp, log


def apply_function(func, valor):
    opciones = {"sin": sin, "cos": cos, "tan": tan, "exp": exp, "log": log}
    resultado = {}
    for i in range(1, valor+1):
        resultado[i] = opciones[func](i)
    return resultado


def calculadora():
    funcion = input("Elige la operacion a realizar: ")
    num = int(input("Elige el numero: "))
    diccionario = apply_function(funcion, num)
    for value in diccionario.keys():
        print(value, "\t", diccionario[value])


calculadora()
