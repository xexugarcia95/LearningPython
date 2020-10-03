class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frenar = True

    def estado(self):
        print("Marca;", self.marca, "\nModelo;", self.modelo, "\nEn marcha;",
              self.enmarcha, "\nAcelerando;", self.acelera, "\nFrenando;",
              self.frena)


class Furgoneta(Vehiculo):

    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


class Moto(Vehiculo):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca;", self.marca, "\nModelo;", self.modelo, "\nEn marcha;",
              self.enmarcha, "\nAcelerando;", self.acelera, "\nFrenando;",
              self.frena, "\nCaballito;", self.hcaballito)


class VElectrico:
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


miMoto = Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()
miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))


class BicicletaElectrica(VElectrico, Vehiculo):
    pass


miBici = BicicletaElectrica()
