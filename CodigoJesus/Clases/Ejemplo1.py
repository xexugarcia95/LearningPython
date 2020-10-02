class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4  # Encapsulación --> privada
        self.__enMarcha = False

    # Para ser un método en vez de función, debe tener self
    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha:
            chequeo = self.__chequeo_interno()

        if self.__enMarcha and chequeo:
            return "El coche está en marcha"
        elif self.__enMarcha and not chequeo:
            return "Algo ha ido mal en el chequeo, no se puede arrancar"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas, un ancho de",
              self.__anchoChasis, "y un largo de", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno...")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok"
                and self.puertas == "cerradas"):
            return True
        else:
            return False


miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()


print("A continuacion creamos el segundo coche")

miCoche2 = Coche()
print(miCoche2.arrancar(False))

miCoche2.estado()
