class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4  # Encapsulación --> privada
        self.enMarcha = False

    # Para ser un método en vez de función, debe tener self
    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos

        if self.enMarcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas, un ancho de",
              self.__anchoChasis, "y un largo de", self.__largoChasis)


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print("A continuacion creamos el segundo coche")

miCoche2 = Coche()
print(miCoche2.arrancar(False))

miCoche2.__ruedas = 5
miCoche2.estado()
