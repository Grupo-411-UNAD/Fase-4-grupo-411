
import os
from datetime import datetime

def registrar_log(mensaje):
    # Crear carpeta logger si no existe
    if not os.path.exists("logger.py"):
        os.makedirs("logger.py")

    # Ruta dentro de la carpeta
    ruta = "logger.py/logs.txt"

    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} -> {mensaje}\n")



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

