"""Escribir un programa que pregunte el nombre del usuario en la consola y
después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene
<n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n>
es el número de letras que tienen el nombre."""

mi_nombre = input("Introduce tu nombre: ")

# La funcion upper te comvierte el str en mayusculas
print("El nombre " + mi_nombre.upper() + " tiene " + str(len(mi_nombre))
      + " letras")
