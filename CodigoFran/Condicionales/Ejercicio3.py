"""Escribir un programa que pida al usuario dos
números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar
un error."""

numero1 = input("Introduzca el primer numero: ")
numero2 = input("Introduzca el segundo numero: ")

if int(numero2) == 0:
    print("ERROR")
else:
    division = int(numero1)/int(numero2)
    print(f"La division es: {division}")
