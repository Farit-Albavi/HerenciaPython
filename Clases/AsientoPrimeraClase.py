from Clases.Asiento import Asiento 

#Clase que representa un asiento extra comodo de primera clase de un vuelo
class AsientoPrimeraClase(Asiento):

    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base
        self.inicial: int = (5) # Establece la capacidad maxima de asientos disponibles
        self.disponibles: int = (self.inicial) # Establece el número disponible de asientos de primera clase
        # Atributos propios
        self.__reclinacion: bool = True
        self.__wifi: bool = True
        self.__entretenimiento: bool = True

    # Metodos propios de la clase ->
    def atencion_personalizada(self):
        print("Ha solicitado atención personalizada. Un miembro de la tripulación lo atenderá pronto.")

    def seleccionar_platillos(self):
        print("Ha solicitado el menú de platillos. Un miembro de la tripulación le traerá la carta pronto.")
            
    # Metodos heredados de la superclase
    def calcular_precio(self):
        # Cálculo del precio del asiento de primera clase
        return 1000

    def reservar(self, cantidad):
        # Reserva una cantidad predefinida de asientos
        if self.disponibles > 0 and cantidad <= self.disponibles and cantidad > 0:
            self.disponibles -= cantidad
            print(f"Asientos de primera clase disponible: {self.disponibles}")
            return True
        else:
            print("\n### No hay asientos disponibles para la cantidad que desea comprar. ###\n")
            return False