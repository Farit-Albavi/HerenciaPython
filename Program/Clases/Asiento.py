from abc import ABC, abstractmethod

class Asiento(ABC):
    """Clase abstracta de asientos"""

    def __init__(self):
        self.__inicial: int = 0
        self.__disponibles: int = 0

    @abstractmethod
    def calcular_precio(self):
        pass

    @abstractmethod
    def reservar(self, cantidad):
        pass

