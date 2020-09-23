"""Escribir un programa que pregunte al usuario por
el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde."""

horas = input("Cuantas horas has trabajado?: ")
precio = input("Cuanto se paga la hora?: ")

paga = int(horas)*float(precio)

print(f"El salario que le corresponde es: {paga} euros")
