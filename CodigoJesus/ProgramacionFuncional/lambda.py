# Estructura de una función lambda
# lambda argumentos : cuerpo de la funcion


def suma(val1=0, val2=0): return val1+val2


def operacion(operacion, val1=0, val2=0): return operacion(val1, val2)


resultado = operacion(suma, 10, 20)
print(resultado)
