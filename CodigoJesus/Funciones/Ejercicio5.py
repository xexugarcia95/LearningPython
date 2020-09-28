"""Escribir una función que calcule el área de un círculo y otra que calcule
el volumen de un cilindro usando la primera función."""


def areaCirculo(radio):
    return 3.14*radio**2


def volumenCilindro(radio, altura):
    return areaCirculo(radio)*altura


print(areaCirculo(2))
print(volumenCilindro(2, 4))
