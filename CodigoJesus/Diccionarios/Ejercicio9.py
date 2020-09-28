"""Escribir un programa que gestione las facturas pendientes de cobro de una
empresa. Las facturas se almacenarán en un diccionario donde la clave de cada
factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura,
 pagar una existente o terminar. Si desea añadir una nueva factura se
 preguntará por el número de factura y su coste y se añadirá al diccionario.
 Si se desea pagar una factura se preguntará por el número de factura y se
 eliminará del diccionario. Después de cada operación el programa debe mostrar
 por pantalla la cantidad cobrada hasta el momento y la cantidad
 pendiente de cobro."""


diccionario = {}
pendiente = 0
pagado = 0
print("Menú. Opciones\n1.Añadir Factura\n2.Pagar Factura\n3.Salir")
eleccion = int(input("Elige una opción: "))
while eleccion != 3:
    if eleccion == 1:
        clave = input("Introduce clave de la factura: ")
        valor = float(input("Introduce coste de la factura: "))
        diccionario[clave] = valor
        pendiente += diccionario.get(clave)
    elif eleccion == 2:
        clave = input("Introduce la clave de la factura a pagar: ")
        if clave in diccionario:
            print("La cantidad de pagar es de " + str(diccionario.get(clave)))
            pendiente -= diccionario.get(clave)
            pagado += diccionario.get(clave)
            del diccionario[clave]
        else:
            print("Esta factora no existe en la Base de datos")
    else:
        print("Tu elección no existe o no está implementada aún, por favor,"
              + " elige otra opción")

    print("Facturas actuales del diccionario: " + str(list(diccionario.keys())))
    print("Pago pendiente: " + str(round(pendiente, 2)) + "\tPagado: " + str(round(pagado, 2)))
    eleccion = int(input("Elige una opción: "))
