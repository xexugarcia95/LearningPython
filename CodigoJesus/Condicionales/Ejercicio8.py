"""En una determinada empresa, sus empleados son evaluados al final de cada año.
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre
las cifras mencionadas. A continuación se muestra una tabla con los niveles
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada
nivel es de 2.400€ multiplicada por la puntuación del nivel.Escribir un programa
que lea la puntuación del usuario e indique su nivel de rendimiento, así como
la cantidad de dinero que recibirá el usuario."""

punto = float(input("Introduce tu puntuacion: "))
print("Dinero conseguido: " + str(punto*2400))
if punto == 0.0:
    print("Inaceptable")
elif punto == 0.4:
    print("Aceptable")
elif punto >= 0.6:
    print("Meritorio")
else:
    print(", pero el valor no es válido")
