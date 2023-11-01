from Asiento import Asiento

class AsientoEconomico(Asiento):

    def __init__(self: str):
        super().__init__() 
        self.inicial: int = (18) # Establece la capacidad maxima de asientos disponibles
        self.disponibles: int = (self.inicial) # Establece el número disponible de asientos económicos

    # Metodos heredados de la super clase
    def calcular_precio(self):
        # Cálculo del precio del asiento económico
        return 200

    def reservar(self, cantidad):
        # Reserva una cantidad predefinida de asientos
        if self.disponibles > 0 and cantidad <= self.disponibles and cantidad > 0:
            self.disponibles -= cantidad
            print(f"Asientos economicos disponibles: {self.disponibles}")
            return True
        else:
            print("\n### No hay asientos disponibles para la cantidad que desea comprar. ###\n")
            return False