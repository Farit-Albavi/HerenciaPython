from abc import ABCMeta,abstractmethod
from Boleteria import Boleteria
from Empresa import Empresa


class Aerolinea(Empresa):
    def __init__(self):
        self.boleteria = Boleteria()
    __metaclass__ = ABCMeta 
    pass

aerolinea = Aerolinea()