# Importación de módulos necesarios para la implementación de la clase Reserva,
# así como para el manejo de excepciones y la interacción con las clases Cliente y Servicio.
import excepciones

class Reserva():
    def __init__(self, cliente, servicio, duracion):
        try:
            if duracion <= 0:
                raise excepciones.ReservaError("duracion mala")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "pendiente"

        except Exception as e:
            excepciones.logging.error("error en reserva " + str(e))
            print("error creando reserva")

    def confirmar(self):
        self.estado = "confirmada"

    def cancelar(self):
        self.estado = "cancelada"

    def calcular_total(self):
        try:
            return self.servicio.calcular_costo()
        except Exception as e:
            excepciones.logging.error("error calculo " + str(e))
            print("error en calculo")
            return 0

    def mostrar(self):
        try:
            return self.cliente.nombre + " - " + self.servicio.descripcion() + " - " + self.estado
        except Exception as e:
            excepciones.logging.error("error mostrando " + str(e))
            return "no se pudo mostrar"
#He analizado el codigo en VS y aparecen errores en amarillo verifiquen lo que hemos hecho, hago más???