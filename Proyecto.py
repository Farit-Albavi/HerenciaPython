from Clases.Asiento import Asiento
from Clases.AsientoPrimeraClase import AsientoPrimeraClase
from Clases.AsientoEconomico import AsientoEconomico



print("¡Bienvenidos a Python Airlines!")

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
    print(f"""=== Disponibilidad de asientos ===
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

#Calcula el precio total acumulando en lista de reservas, sumando el precio de cada reserva individual
for reserva in reservas:
    total_precio += reserva.calcular_precio()


#Calculos de la cantidad de reservas segun la clase de asiento    
cantidadPrimeraAdquirido = asientos_primera_clase.inicial - asientos_primera_clase.disponibles   
cantidadEconomicoAdquierido = asientos_economicos.inicial - asientos_economicos.disponibles  

#Calculos de premio por cada tipo de asiento
precioPrimeraClase = asientos_primera_clase.calcular_precio()
precioClaseEconomico = asientos_economicos.calcular_precio()

print(f"""=== Datos de las compras ===
    Asientos de primera clase adquiridos: {cantidadPrimeraAdquirido}. Costo: $ {precioPrimeraClase * cantidadPrimeraAdquirido}
    Asientos economicos adquiridos: {cantidadEconomicoAdquierido}. Costo: $ {precioClaseEconomico * cantidadEconomicoAdquierido}
    Total a pagar por los asientos: ${total_precio}""")

