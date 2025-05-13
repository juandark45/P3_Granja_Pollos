# Pollos.py
class Pollo:
    def __init__(self, codigo, raza, edad):
        self.__codigo = codigo
        self.__raza = raza
        self.__edad = edad
        self.__produccion_huevos = {} 

 
    def get_codigo(self):
        return self.__codigo

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    def get_produccion(self):
        return self.__produccion_huevos

 
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        self.__edad = edad

   
    def registrar_huevos(self, semana, cantidad):
        self.__produccion_huevos[semana] = cantidad

    def obtener_produccion_semanal(self, semana):
        return self.__produccion_huevos.get(semana, 0)

    def obtener_produccion_total(self):
        return sum(self.__produccion_huevos.values())
