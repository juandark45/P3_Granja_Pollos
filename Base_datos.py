from interfase import ICrud
from Pollos import Pollo

class BaseDatos(ICrud):
    def __init__(self):
        self.pollos = {}  # clave: codigo, valor: objeto Pollo

    def crear_pollo(self, pollo):
        if pollo.get_codigo() in self.pollos:
            print("[!] El pollo ya existe.")
        else:
            self.pollos[pollo.get_codigo()] = pollo
            print("[+] Pollo registrado correctamente.")

    def leer_pollo(self, codigo):
        pollo = self.pollos.get(codigo)
        if pollo:
            print(f"\nCódigo: {pollo.get_codigo()}\nRaza: {pollo.get_raza()}\nEdad: {pollo.get_edad()}\nProducción Total: {pollo.obtener_produccion_total()} huevos\n")
        else:
            print("[!] Pollo no encontrado.")

    def actualizar_pollo(self, codigo, **kwargs):
        pollo = self.pollos.get(codigo)
        if pollo:
            if 'codigo' in kwargs:
                nuevo_codigo = kwargs['codigo']
                pollo.set_codigo(nuevo_codigo)
                self.pollos[nuevo_codigo] = pollo
                del self.pollos[codigo]
            if 'raza' in kwargs:
                pollo.set_raza(kwargs['raza'])
            if 'edad' in kwargs:
                pollo.set_edad(kwargs['edad'])
            print("[*] Pollo actualizado.")
        else:
            print("[!] Pollo no encontrado.")

    def eliminar_pollo(self, codigo):
        if codigo in self.pollos:
            del self.pollos[codigo]
            print("[-] Pollo eliminado.")
        else:
            print("[!] Pollo no encontrado.")

    def registrar_produccion(self, codigo, semana, cantidad):
        pollo = self.pollos.get(codigo)
        if pollo:
            pollo.registrar_huevos(semana, cantidad)
            print("[+] Producción registrada.")
        else:
            print("[!] Pollo no encontrado.")

    def mostrar_todos(self):
        if not self.pollos:
            print("[!] No hay pollos registrados.")
        else:
            for codigo, pollo in self.pollos.items():
                print(f"Código: {pollo.get_codigo()}, Raza: {pollo.get_raza()}, Edad: {pollo.get_edad()}, Total Huevos: {pollo.obtener_produccion_total()}")
