"""Escribir un programa que pida al usuario dos números y muestre por pantalla
su división. Si el divisor es cero el programa debe mostrar un error."""

val_1 = int(input("Primer valor: "))
val_2 = int(input("Segundo valor: "))

if val_2 == 0:
    print("Error!!!")
else:
    print(str(val_1/val_2))
