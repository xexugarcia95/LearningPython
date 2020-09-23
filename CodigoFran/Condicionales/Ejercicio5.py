"""Para tributar un determinado impuesto se debe ser mayor de 16 años
y tener unos ingresos iguales o superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos
mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

edad = input("Introduce tu edad: ")
ingreso = input("Introduce tus ingresos: ")

if int(edad) >= 16 and int(ingreso) >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")
