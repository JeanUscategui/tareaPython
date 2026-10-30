class Maquina:
    def __init__(self, tipo, modelo, velocidad, encendida):
        self.tipo = tipo
        self.modelo = modelo
        self.velocidad = velocidad
        self.encendida = encendida

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_velocidad(self):
        return self.velocidad

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def get_encendida(self):
        return self.encendida

    def set_encendida(self, encendida):
        self.encendida = encendida

    def encender(self):
        self.encendida = True
        print("maquina encendida")

    def apagar(self):
        self.encendida = False
        print("maquina apagada")

    def mover(self):
        print("la maquina se esta moviendo")

    def agarrar_pieza(self):
        print("la maquina agarro una pieza")

    def poner_vidrio(self):
        print("la maquina puso el vidrio del carro")

    def mostrar(self):
        print("tipo:", self.tipo)
        print("modelo:", self.modelo)
        print("velocidad:", self.velocidad)
        print("encendida:", self.encendida)
