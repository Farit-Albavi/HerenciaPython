from abc import ABC, abstractmethod

print("¡Bienvenidos a Python Airlines!")

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


class AsientoPrimeraClase(Asiento):
    """Clase que representa un asiento extra comodo de primera clase de un vuelo"""

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


class AsientoEconomico(Asiento):
    """Clase que representa un asiento generico economico de un vuelo."""

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


# Crear asientos con la cantidad inicial disponible
asientos_primera_clase = AsientoPrimeraClase()
asientos_economicos = AsientoEconomico("ventana")

print("""
=== Precios ===
Asiento de primera clase: 1000$.
Asiento económico: 200$.
""")

# Lista que se utiliza para realizar un seguimiento de los asientos que se han reservado durante la ejecución del programa.
reservas = []


def reservar_asientos(asiento, cantidad, reservas):
    if asiento.reservar(cantidad):
        for i in range(cantidad):
            reservas.append(asiento())
        return True
    else:
        return False


# Reservar asientos
while True:
    print(f"""
=== Disponibilidad de asientos ===
Asiento de primera clase disponible: {asientos_primera_clase.disponibles}
Asiento económico disponible: {asientos_economicos.disponibles}""")

    opcion = input("\nPresiona 1 para comprar un asiento o cualquier otra tecla para salir: ")
    if opcion == "1":
        clase = input("\nIngresa 'primera' para primera clase o 'economico' para clase económica: ")
        if clase == "primera":
            nro_reserva = int(input("Ingrese la cantidad de boletos a reservar: "))
            if asientos_primera_clase.reservar(nro_reserva):
                # Agrega nro_reserva veces el asiento seleccionado en la lista de reservas
                for i in range(nro_reserva):
                    reservas.append(AsientoPrimeraClase())
        elif clase == "economico":
            nro_reserva = int(input("Ingrese la cantidad de boletos a reservar: "))
            if asientos_economicos.reservar(nro_reserva):
                # Agrega nro_reserva veces el asiento seleccionado en la lista de reservas
                for i in range(nro_reserva):
                    reservas.append(AsientoEconomico("ventana"))
        else:
            print("\n### Respuesta incorrecta, vuelva a introducir ###")
    else:
        break

total_precio = 0

# Calcula el precio total acumulando en lista de reservas, sumando el precio de cada reserva individual
for reserva in reservas:
    total_precio += reserva.calcular_precio()


#Calculos de la cantidad de reservas segun la clase de asiento    
cantidadPrimeraAdquirido = asientos_primera_clase.inicial - asientos_primera_clase.disponibles   
cantidadEconomicoAdquierido = asientos_economicos.inicial - asientos_economicos.disponibles  

#Calculos de premio por cada tipo de asiento
precioPrimeraClase = asientos_primera_clase.calcular_precio()
precioClaseEconomico = asientos_economicos.calcular_precio()

print(f"""
=== Datos de las compras ===
Asientos de primera clase adquiridos: {cantidadPrimeraAdquirido}. Costo: $ {precioPrimeraClase * cantidadPrimeraAdquirido}
Asientos economicos adquiridos: {cantidadEconomicoAdquierido}. Costo: $ {precioClaseEconomico * cantidadEconomicoAdquierido}
Total a pagar por los asientos: ${total_precio}
""")

