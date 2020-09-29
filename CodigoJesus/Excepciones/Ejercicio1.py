def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operación errónea"


op1 = int(input("introduce un operador: "))
op2 = int(input("Introduce otro operador: "))

print(division(op1, op2))
