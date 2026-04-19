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
    
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_marca(self,nueva_marca):
        self.__marca = nueva_marca

    def set_modelo(self,nuevo_modelo):
        self.__modelo = nuevo_modelo
    
    def set_almacenamiento(self,nuevo_almacenamiento):
        self.__almacenamiento = nuevo_almacenamiento
    
    def set_memoria(self,nueva_memoria):
        self.__memoria = nueva_memoria

    def set_bateria(self,nueva_bateria):
        self.__bateria = nueva_bateria

    def info(self):
        print("Informacion del celular:")
        print(f"Nombre: {self.__nombre}, Marca: {self.__marca}, Modelo: {self.__modelo}")
        print(f"Almacenamiento: {self.__almacenamiento}, Memoria: {self.__memoria}, Bateria: {self.__bateria}")

    def jugar(self,horas):
        consumo = horas * 10
        if self.__bateria >= consumo:
            self.__bateria -= consumo
            print(f"Jugaste {horas} horas, Bateria restante: {self.__bateria}%")
        else:
            self.__bateria = 0
            print("Se agoto la bateria, Apagando celular...")