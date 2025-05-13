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
