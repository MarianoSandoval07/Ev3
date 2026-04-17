class Celular:
    def __init__(self,nombre,marca,modelo,almacenamiento,memoria,bateria):
        self.__nombre = nombre
        self.__marca = marca
        self.__modelo = modelo
        self.__almacenamiento = almacenamiento
        self.__memoria = memoria
        self.__bateria = bateria

    def get_nombre(self):
        return self.__nombre
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_almacenamiento(self):
        return self.__almacenamiento
    
    def get_memoria(self):
        return self.__memoria
    
    def get_bateria(self):
        return self.__bateria