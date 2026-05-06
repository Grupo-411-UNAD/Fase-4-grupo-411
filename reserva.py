# Importación de módulos necesarios para la implementación de la clase Reserva,
# así como para el manejo de excepciones y la interacción con las clases Cliente y Servicio.
import excepciones

Reservas_Creadas = [] # Lista global para almacenar las reservas creadas

# ============================================================
# CLASE RESERVA
# ============================================================

class Reserva():
    def __init__(self, cliente, servicio, duracion):
        try:
            if duracion <= 0:
                raise excepciones.ReservaError("La duración de la reserva debe ser mayor que cero.")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "Pendiente"
            Reservas_Creadas.append(self)
        except Exception as e:
            excepciones.logging.error("Error en reserva " + str(e))
            print("Error creando reserva")

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def calcular_total(self):
        try:
            return self.servicio.calcular_costo()
        except Exception as e:
            excepciones.logging.error("Error en cálculo " + str(e))
            print("Error en cálculo")
            return 0

    def mostrar(self):
        try:
            return self.cliente.nombre + " - " + self.servicio.descripcion() + " - " + self.estado
        except Exception as e:
            excepciones.logging.error("Error al mostrar " + str(e))
            print("Error al mostrar datos de reserva")
            return "No se pudo mostrar"
