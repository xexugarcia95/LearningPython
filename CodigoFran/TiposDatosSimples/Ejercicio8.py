"""Escribir un programa que pida al usuario su peso (en kg) y
estatura (en metros), calcule el índice de masa corporal y
lo almacene en una variable, y muestre por pantalla la frase
Tu índice de masa corporal es <imc> donde <imc> es el índice
de masa corporal calculado redondeado con dos decimales."""

peso = input("Introduzca su peso en kg ")
estatura = input("Introduzca su estatura en metros ")

imc = float(peso)/(float(estatura)**2)
imc = round(imc, 2)

print(f"El indice de masa corporal es: {imc}")

"""con round(a,b) podemos redondear un numero (a) donde (b)
es el numero de decimales con los que nos queremos quedar"""
