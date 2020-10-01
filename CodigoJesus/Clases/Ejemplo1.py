class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    # Para ser un método en vez de función, debe tener self
    def arrancar(self):
        self.enMarcha = True

    def estado(self):
        if self.enMarcha:
            print("El coche está en marcha")
        else:
            print("El coche está parado")


miCoche = Coche()
miCoche.estado()
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene", miCoche.ruedas, "ruedas")

miCoche.arrancar()
miCoche.estado()
