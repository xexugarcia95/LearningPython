def suma(val1=0, val2=0):
    return val1+val2


def operacion(funcion, val1=0, val2=0):
    return funcion(val1, val2)


funcion_suma = suma
resultado = operacion(funcion_suma, 10, 20)
print(resultado)
