import logging

logging.basicConfig(filename="logs.txt", level=logging.ERROR)

# Definición de excepciones personalizadas para el manejo de errores específicos del sistema

class ClienteError(Exception):
    # Excepción para errores relacionados con clientes.
    pass

class ServicioError(Exception):
    # Excepción para errores relacionados con servicios.
    pass

class ReservaError(Exception):
    # Excepción para errores relacionados con reservas.
    pass

