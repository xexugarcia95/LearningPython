"""Escribir un programa que pregunte al usuario por el número de horas
trabajadas y el coste por hora. Después debe mostrar por pantalla la paga
que le corresponde."""

horas = int(input("Numero de horas trabajadas: "))
coste = int(input("Coste por hora: "))
print("Paga = " + str(horas*coste) + "€")
