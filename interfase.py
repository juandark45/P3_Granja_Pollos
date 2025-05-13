from abc import ABC, abstractmethod

class ICrud(ABC):
    @abstractmethod
    def crear_pollo(self, pollo): pass

    @abstractmethod
    def leer_pollo(self, codigo): pass

    @abstractmethod
    def actualizar_pollo(self, codigo, **kwargs): pass

    @abstractmethod
    def eliminar_pollo(self, codigo): pass

def menu():
    bd = BaseDatos()

    while True:
        print("\n--- Menú de la Granja ---")
        print("1. Registrar nuevo pollo")
        print("2. Consultar pollo")
        print("3. Actualizar datos del pollo")
        print("4. Eliminar pollo")
        print("5. Registrar producción semanal")
        print("6. Mostrar todos los registros")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del pollo: ")
            raza = input("Raza: ")
            edad = input("Edad: ")
            pollo = Pollo(codigo, raza, edad)
            bd.crear_pollo(pollo)

        elif opcion == "2":
            codigo = input("Código del pollo: ")
            bd.leer_pollo(codigo)

        elif opcion == "3":
            codigo = input("Código actual del pollo: ")
            nuevo_codigo = input("Nuevo código (dejar en blanco para mantener): ")
            nueva_raza = input("Nueva raza (dejar en blanco para mantener): ")
            nueva_edad = input("Nueva edad (dejar en blanco para mantener): ")
            cambios = {}
            if nuevo_codigo: cambios['codigo'] = nuevo_codigo
            if nueva_raza: cambios['raza'] = nueva_raza
            if nueva_edad: cambios['edad'] = nueva_edad
            bd.actualizar_pollo(codigo, **cambios)

        elif opcion == "4":
            codigo = input("Código del pollo a eliminar: ")
            bd.eliminar_pollo(codigo)

        elif opcion == "5":
            codigo = input("Código del pollo: ")
            semana = input("Semana (ej: Semana1): ")
            cantidad = int(input("Cantidad de huevos: "))
            bd.registrar_produccion(codigo, semana, cantidad)

        elif opcion == "6":
            bd.mostrar_todos()

        elif opcion == "7":
            print("[!] Saliendo del sistema.")
            break

        else:
            print("[!] Opcion no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
