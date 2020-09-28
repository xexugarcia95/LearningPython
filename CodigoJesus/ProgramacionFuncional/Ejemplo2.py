def crear_funcion(operador):
    if operador == '+':
        def suma(val1=0, val2=0):
            return val1+val2
        return suma


def operacion(funcion, val1=0, val2=0):
    return funcion(val1, val2)


funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma, 10, 20)
print(resultado)
