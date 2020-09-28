"""Escribir un programa que pregunte por una muestra de números,
separados por comas, los guarde en una lista y muestre por pantalla su media y
desviación típica."""

lista = []
for i in range(5):
    lista.append(int(input("Introduce un numero: ")))

cont = 0
cont2 = 0
for i in range(5):
    cont += lista[i]
cont /= 5

for i in range(5):
    cont2 += (lista[i]-cont)**2
cont2 /= 5
cont2 = cont2**(1/2)

print("La media es " + str(cont) + " y la desviación típica es "
      + str(round(cont2, 2)))
