"""Escribir un programa que permita gestionar la base de datos de clientes
de una empresa. Los clientes se guardarán en un diccionario en el que la clave
de cada cliente será su NIF, y el valor será otro diccionario con los datos
del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente
tendrá el valor True si se trata de un cliente preferente. El programa debe
preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente,
(2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
(5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida
el programa tendrá que hacer lo siguiente:
    1.Preguntar los datos del cliente, crear un diccionario con los datos y
    añadirlo a la base de datos.
    2.Preguntar por el NIF del cliente y eliminar sus datos de la base de datos
    3.Preguntar por el NIF del cliente y mostrar sus datos.
    4.Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    5.Mostrar la lista de clientes preferentes de la base de datos con su NIF
    y nombre.
    6.Terminar el programa."""

diccionario = {}

print("Bienvenido al sistema de administración de clientes")
print("\t1.Añadir cliente\n\t2.Eliminar cliente\n\t3.Mostrar cliente\n\t"
      + "4.Listar clientes\n\t5.Listas clientes preferentes\n\t6.Terminar")
opcion = int(input("Por favor, elija una opción: "))

while opcion != 6:
    if opcion == 1:
        NIF = input("Introduce tu NIF: ")
        subdiccionario = {}
        nombre = input("Introduce tu nombre: ")
        subdiccionario["nombre"] = nombre
        direccion = input("Introduce tu direccion: ")
        subdiccionario["direccion"] = direccion
        telefono = input("Introduce tu teléfono: ")
        subdiccionario["telefono"] = telefono
        correo = input("Introduce tu correo: ")
        subdiccionario["correo"] = correo
        preferente = input("¿Es preferente?(S/N): ")
        if preferente == 'S':
            subdiccionario["preferente"] = True
        else:
            subdiccionario["preferente"] = False
        diccionario[NIF] = subdiccionario
    elif opcion == 2:
        NIF = input("Introduce el NIF del usuario a eliminar: ")
        if NIF in diccionario.keys():
            del diccionario[NIF]
        else:
            print("No existe ese usuario en la base de datos")
    elif opcion == 3:
        NIF = input("Introduce el NIF del cliente:")
        if NIF in diccionario:
            usuario = diccionario[NIF]
            print("----------------------------------------------------------")
            print(usuario["nombre"] + "\t" + usuario["direccion"] + "\t"
                  + usuario["telefono"] + "\t" + usuario["correo"] + "\t"
                  + str(usuario["preferente"]))
        else:
            print("El NIF introducido no existe")

    elif opcion == 4:
        usuarios = diccionario.values()
        print("Nombre\tDireccion\tTeléfono\tCorreo\tPreferente")
        print("-------------------------------------------------------------")
        for usuario in usuarios:
            print(usuario["nombre"] + "\t" + usuario["direccion"] + "\t"
                  + usuario["telefono"] + "\t" + usuario["correo"] + "\t"
                  + str(usuario["preferente"]))
    elif opcion == 5:
        usuarios = diccionario.values()
        print("Nombre\tDireccion\tTeléfono\tCorreo\tPreferente")
        print("--------------------------------------------------------------")
        for usuario in usuarios:
            if usuario["preferente"] is True:
                print(usuario["nombre"] + "\t" + usuario["direccion"] + "\t"
                      + usuario["telefono"] + "\t" + usuario["correo"] + "\t"
                      + str(usuario["preferente"]))
    opcion = int(input("Por favor, elija una opción: "))
