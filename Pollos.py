class pollos:
    #metodo constructor 
    def __init__(self, id_pollo, dato_edad):
        self.codigo_pollo = id_pollo
        self.dato_edad = dato_edad
        #llamados de otras clases 
        self.objeto_datos = base_datos() #el objeto de la clase 

#metodo publico de modificacion atributo
    def getCodigo_pollo(self):
        return self.codigo_pollo
    
    def setCodigo_pollo(self, codigo_pollo):
        self.codigo_pollo = codigo_pollo

#metodos para conextar base datos
def guardar_pollo(self):
