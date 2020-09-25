"""Alteración del ejercicio 13, donde leo una cadena de números separados
por comas"""

numeros = input("Introduce una serie de números separados por coma: ")
numeros = numeros.split(',')
print(numeros[:])
cont = 0
for i in range(len(numeros)):
    cont+=int(numeros[i])
cont/=len(numeros)
cont2 = 0
for i in range(len(numeros)):
    cont2+= (int(numeros[i])-cont)**2
cont2/=len(numeros)
cont2 = cont2**(1/2)

print("La media es " + str(cont) + " y la desviación típica es " + str(round(cont2,2)))
