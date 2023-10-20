from Clases.Asiento import Asiento

#Clase que representa un asiento generico economico de un vuelo.
class AsientoEconomico(Asiento):

    def __init__(self, ubicacion: str):
        super().__init__()  # Llama al constructor de la clase base
        self.inicial: int = (10) # Establece la capacidad maxima de asientos disponibles
        self.disponibles: int = (self.inicial) # Establece el número disponible de asientos económicos
        self.__ubicacion: str = ubicacion  # Puede ser "ventana" o "pasillo"



    # Metodos propios de la clase ->
    def equipaje_extra(self, cantidad: int = 0):
        costo_por_equipaje_extra: float = 50.0  # Supongamos que hay un costo fijo por cada pieza de equipaje adicional.
        costo_total = cantidad * costo_por_equipaje_extra
        print(f"Se han agregado {cantidad} piezas de equipaje extra. Costo adicional: ${costo_total}")


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