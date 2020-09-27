"""Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas
que el usuario tiene que repetir."""

encontrado = False
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
suspenso = []

for i in range(len(asignaturas)):
    while not encontrado:
        nota = int(input("Introduce la nota de "+asignaturas[i]+": "))
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            encontrado = True
        else:
            print("Nota incorrecta.")
    encontrado = False
print()
for i in range(len(notas)):
    print(f"{asignaturas[i]} tiene una nota de: {notas[i]}")
print()


for i in range(len(notas)):
    if(notas[i] < 5):
        suspenso.append(asignaturas[i])

print("Tienes que repetir: ")
for i in range(len(suspenso)):
    print(f"-{suspenso[i]}")
