# --------------------------------------------------------------------------------------------------------------------------------------------
# Importación de módulos necesarios para el manejo de archivos, fechas y horas, así como para la definición de excepciones personalizadas
# --------------------------------------------------------------------------------------------------------------------------------------------
import os
from datetime import datetime
# --------------------------------------------------------------------------------------------------------------------------------------------
# Función para registrar eventos importantes del sistema en un archivo de logs
# --------------------------------------------------------------------------------------------------------------------------------------------
def registrar_log(mensaje):
    """
    Función para registrar eventos importantes del sistema en un archivo de logs.
    Recibe un mensaje como parámetro y lo escribe en un archivo de texto con una marca de tiempo."""
    if not os.path.exists("logger"):
        os.makedirs("logger")
    # ----------------------------------
    # Especificar ruta dentro de la carpeta
    # ----------------------------------
    ruta = "logger/logs.txt"
    # -------------------------------------------------------------------------
    # Abrir el archivo en modo append para no sobrescribir los logs anteriores
    # -------------------------------------------------------------------------
    with open(ruta, "a", encoding="utf-8") as archivo: 
        archivo.write(f"{datetime.now()} -> {mensaje}\n")

# --------------------------------------------------------------------------------------------------------------------------------------------
# Definición de excepciones personalizadas para el manejo de errores específicos del sistema
# --------------------------------------------------------------------------------------------------------------------------------------------
class ClienteError(Exception):
    # Excepción para errores relacionados con clientes.
    pass

class ServicioError(Exception):
    # Excepción para errores relacionados con servicios.
    pass

class ReservaError(Exception):
    # Excepción para errores relacionados con reservas.
    pass

