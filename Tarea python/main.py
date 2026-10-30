from empleado import Empleado
from objeto import Objeto
from maquina import Maquina
from carro import Carro

e = Empleado("Carlos", 35, "operario", "mañana")
o = Objeto("tablet", "Samsung", "negro", 80)
m = Maquina("brazo robotico", "R200", 5, False)
c = Carro("Mazda", "3", "blanco", 4)

print("EMPLEADO")
e.mostrar()
e.saludar()
e.trabajar()
e.usar_tablet()
print()

print("OBJETO")
o.mostrar()
o.encender()
o.enviar_orden()
o.usar()
print()

print("MAQUINA")
m.mostrar()
m.encender()
m.mover()
m.agarrar_pieza()
m.poner_vidrio()
print()

print("CARRO")
c.mostrar()
c.pintar("rojo")
c.encender()
c.acelerar()
c.frenar()
print()

e.set_turno("noche")
print("el turno ahora es", e.get_turno())
m.set_velocidad(10)
print("la velocidad ahora es", m.get_velocidad())
