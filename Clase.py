class Ventana:
    __titulo:str
    __valorX1:int
    __valorY1:int
    __valorXS:int
    __valorYS:int

    def __init__(self, titulo=None, valorX1=0, valorY1=0, valorXS=500, valorYS=500):
        self.__titulo = titulo
        self.__valorX1 = max(0, valorX1)
        self.__valorY1 = max(0, valorY1)
        self.__valorXS = min(500, valorXS)
        self.__valorYS = min(500, valorYS)

    def get_titulo(self):
        return self.__titulo

    def get_valorX1(self):
        return self.__valorX1

    def get_valorY1(self):
        return self.__valorY1

    def get_valorXS(self):
        return self.__valorXS

    def get_valorYS(self):
        return self.__valorYS

    def mostrar(self):
        print(f'Ventana: {self.__titulo}, Coordenadas: ({self.__valorX1}, {self.__valorY1}), ({self.__valorXS}, {self.__valorYS})')

    def alto(self):
        return self.__valorYS - self.__valorY1

    def ancho(self):
        return self.__valorXS - self.__valorX1

    def bajar(self, unidades=1):
        self.__valorY1 += unidades
        self.__valorYS += unidades

    def subir(self, unidades=1):
        self.__valorY1 -= unidades
        self.__valorYS -= unidades

    def moverDerecha(self, unidades=1):
        self.__valorX1 += unidades
        self.__valorXS += unidades

    def moverIzquierda(self, unidades=1):
        self.__valorX1 -= unidades
        self.__valorXS -= unidades