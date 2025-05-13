from interfase import ICrud
from Pollos import Pollo

class BaseDatos(ICrud):
    def __init__(self):
        self.pollos = {}

    def crear_pollo(self, pollo):
        if pollo.codigo in self.pollos:
            print("Ya existe un pollo con ese código.")
        else:
            self.pollos[pollo.codigo] = pollo
            print("Pollo registrado.")

    def leer_pollo(self, codigo):
        return self.pollos.get(codigo)

    def actualizar_pollo(self, codigo, **kwargs):
        pollo = self.pollos.get(codigo)
        if pollo:
            if 'raza' in kwargs and kwargs['raza']:
                pollo.raza = kwargs['raza']
            if 'edad' in kwargs and kwargs['edad']:
                pollo.edad = kwargs['edad']
            print("Pollo actualizado.")
        else:
            print("Pollo no encontrado.")

    def eliminar_pollo(self, codigo):
        if codigo in self.pollos:
            del self.pollos[codigo]
            print("Pollo eliminado.")
        else:
            print("Pollo no encontrado.")

    def registrar_produccion(self, codigo, semana, cantidad):
        pollo = self.leer_pollo(codigo)
        if pollo:
            pollo.registrar_huevos(semana, cantidad)
            print("Producción registrada.")
        else:
            print("Pollo no encontrado.")

    def mostrar_todos(self):
        if not self.pollos:
            print("No hay pollos registrados.")
        for pollo in self.pollos.values():
            print(f"\nCódigo: {pollo.codigo}")
            print(f"Raza: {pollo.raza}")
            print(f"Edad: {pollo.edad}")
            print(f"Producción total: {pollo.obtener_produccion_total()} huevos")
            for semana, cant in pollo.produccion_huevos.items():
                print(f"  Semana {semana}: {cant} huevos")from interfase import ICrud
from Pollos import Pollo

class BaseDatos(ICrud):
    def __init__(self):
        self.pollos = {}

    def crear_pollo(self, pollo):
        if pollo.codigo in self.pollos:
            print("Ya existe un pollo con ese código.")
        else:
            self.pollos[pollo.codigo] = pollo
            print("Pollo registrado.")

    def leer_pollo(self, codigo):
        return self.pollos.get(codigo)

    def actualizar_pollo(self, codigo, **kwargs):
        pollo = self.pollos.get(codigo)
        if pollo:
            if 'raza' in kwargs and kwargs['raza']:
                pollo.raza = kwargs['raza']
            if 'edad' in kwargs and kwargs['edad']:
                pollo.edad = kwargs['edad']
            print("Pollo actualizado.")
        else:
            print("Pollo no encontrado.")

    def eliminar_pollo(self, codigo):
        if codigo in self.pollos:
            del self.pollos[codigo]
            print("Pollo eliminado.")
        else:
            print("Pollo no encontrado.")

    def registrar_produccion(self, codigo, semana, cantidad):
        pollo = self.leer_pollo(codigo)
        if pollo:
            pollo.registrar_huevos(semana, cantidad)
            print("Producción registrada.")
        else:
            print("Pollo no encontrado.")

    def mostrar_todos(self):
        if not self.pollos:
            print("No hay pollos registrados.")
        for pollo in self.pollos.values():
            print(f"\nCódigo: {pollo.codigo}")
            print(f"Raza: {pollo.raza}")
            print(f"Edad: {pollo.edad}")
            print(f"Producción total: {pollo.obtener_produccion_total()} huevos")
            for semana, cant in pollo.produccion_huevos.items():
                print(f"  Semana {semana}: {cant} huevos")
