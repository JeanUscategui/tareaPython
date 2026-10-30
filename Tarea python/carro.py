class Carro:
    def __init__(self, marca, modelo, color, puertas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.puertas = puertas

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_puertas(self):
        return self.puertas

    def set_puertas(self, puertas):
        self.puertas = puertas

    def encender(self):
        print("el carro encendio")

    def apagar(self):
        print("el carro se apago")

    def acelerar(self):
        print("el carro esta acelerando")

    def frenar(self):
        print("el carro freno")

    def pintar(self, color):
        self.color = color
        print("el carro se pinto de " + color)

    def mostrar(self):
        print("marca:", self.marca)
        print("modelo:", self.modelo)
        print("color:", self.color)
        print("puertas:", self.puertas)
