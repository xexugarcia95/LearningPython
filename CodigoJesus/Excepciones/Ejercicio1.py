def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        return "Operación errónea"


while True:
    try:
        op1 = int(input("introduce un operador: "))
        op2 = int(input("Introduce otro operador: "))
        break
    except ValueError:
        print("Valor no válido")

try:
    print(division(op1, op2))
except NameError:
    print("Debido a errores previos, las variables no están bien definidas")
