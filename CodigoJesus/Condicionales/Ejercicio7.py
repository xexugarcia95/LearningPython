"""Escribir un programa que pregunte al usuario su renta anual y muestre por
pantalla el tipo impositivo que le corresponde."""

renta = int(input("Renta anual: "))

if renta < 10000:
    print("5%")
elif renta >= 10000 and renta < 20000:
    print("15%")
elif renta >= 20000 and renta < 35000:
    print("30%")
else:
    print("45%")
