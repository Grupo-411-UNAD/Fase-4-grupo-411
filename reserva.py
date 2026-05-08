# Importación de módulos necesarios para la implementación de la clase Reserva,
# así como para el manejo de excepciones y la interacción con las clases Cliente y Servicio.
import excepciones

# ============================================================
# CLASE RESERVA
# ============================================================

class Reserva():
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise excepciones.ReservaError("La duración de la reserva debe ser mayor que cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
            
    def __str__(self):
            return f"Reserva: {self.cliente.nombre} - {self.servicio.nombre} - {self.duracion}h - {self.estado}"

    __repr__ = __str__

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def calcular_total(self):
        try:
            return self.servicio.calcular_costo()
        except Exception as e:
            excepciones.registrar_log("Error en cálculo " + str(e))
            print("Error en cálculo")
            return 0

    def mostrar_informacion(self):
        return (
            f"Reserva | Cliente: {self.cliente} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} horas | Precio: {self.calcular_total()} pesos | Estado: {self.estado}"
        )
    
    @staticmethod
    def crear_reserva(cliente, servicio):
        try:
            print("Creando reserva...")
            duracion = int(input("- Ingrese la duración de la reserva en horas: "))
            reserva = Reserva(cliente, servicio, duracion)
            reserva.estado = "Confirmada"
            return reserva
        except ValueError as e:
            raise ValueError(f"Error: La duración debe ser un número entero válido. {e}")
        except excepciones.ReservaError as e:
            raise e
