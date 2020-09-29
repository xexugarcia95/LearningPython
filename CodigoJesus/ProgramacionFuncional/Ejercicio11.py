"""Escribir una función que reciba una muestra de números y devuelva los
valores atípicos, es decir, los valores cuya puntuación típica sea mayor
que 3 o menor que -3. Nota: La puntuación típica de un valor se obtiene
restando la media y dividiendo por la desviación típica de la muestra."""

from statistics import mean, stdev


def atipico(lista):
    med = mean(lista)
    desv = stdev(lista)

    def func(n):
        puntuacion = (n-med)/desv
        return (puntuacion > 3) or (puntuacion < -3)
    return func


def apply_function(lista):
    return list(filter(atipico(lista), lista))


print(apply_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))
