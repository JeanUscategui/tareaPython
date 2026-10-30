class Empleado:
    def __init__(self, nombre, edad, cargo, turno):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.turno = turno

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_turno(self):
        return self.turno

    def set_turno(self, turno):
        self.turno = turno

    def saludar(self):
        print("hola soy " + self.nombre)

    def trabajar(self):
        print(self.nombre + " esta trabajando")

    def usar_tablet(self):
        print(self.nombre + " esta usando la tablet")

    def revisar_carro(self):
        print(self.nombre + " reviso el carro")

    def descansar(self):
        print(self.nombre + " se fue a descansar")

    def mostrar(self):
        print("nombre:", self.nombre)
        print("edad:", self.edad)
        print("cargo:", self.cargo)
        print("turno:", self.turno)
