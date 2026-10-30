class Objeto:
    def __init__(self, nombre, marca, color, bateria):
        self.nombre = nombre
        self.marca = marca
        self.color = color
        self.bateria = bateria

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_bateria(self):
        return self.bateria

    def set_bateria(self, bateria):
        self.bateria = bateria

    def encender(self):
        print("se encendio la " + self.nombre)

    def apagar(self):
        print("se apago la " + self.nombre)

    def cargar(self):
        self.bateria = 100
        print("bateria cargada")

    def usar(self):
        self.bateria = self.bateria - 10
        print("bateria:", self.bateria)

    def enviar_orden(self):
        print("se envio la orden a la maquina")

    def mostrar(self):
        print("objeto:", self.nombre)
        print("marca:", self.marca)
        print("color:", self.color)
        print("bateria:", self.bateria)
