"""Escribir una función que aplique un descuento a un precio y otra que
aplique el IVA a un precio. Escribir una tercera función que reciba un
diccionario con los precios y porcentajes de una cesta de la compra, y una de
las funciones anteriores, y utilice la función pasada para aplicar los
descuentos o el IVA a los productos de la cesta y devolver el precio final
de la cesta."""


def descuento(precio, descuento):
    return precio-(precio*descuento/100)


def aplicarIVA(precio, iva=21):
    return precio+(precio*iva/100)


def funcion(diccionario, funcion):
    total = 0
    for precio, descuento in diccionario.items():
        total += funcion(precio, descuento)

    return total


print("El precio de la compra con el descuento es: " +
      str(funcion({1000: 20, 500: 10, 100: 1}, descuento)))

print("El precio de la compra con el IVA es: " +
      str(funcion({1000: 20, 500: 10, 100: 1}, aplicarIVA)))
