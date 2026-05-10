#importado asbstractmethod y ABC para crear clases abstractas y métodos abstractos
from abc import ABC, abstractmethod

# Clase cliente que encapsula los datos personales de un cliente
class Cliente():
    # Constructor de la clase Cliente que inicializa los atributos del cliente
    def __init__(self, documento, nombre, telefono):

        self.documento = documento
        self.nombre = nombre
        self.telefono = telefono

    # Métodos getter y setter para acceder y modificar los atributos del cliente desde fuera de la clase

    @property
    def documento(self):
        return self.__documentoCliente

    @documento.setter
    def documento(self, documento):

        if not documento.isdigit():
            raise ClienteError("El documento debe contener solo números")

        if len(documento) < 5:
            raise ClienteError("Documento demasiado corto")

        self.__documentoCliente = documento

    @property
    def nombre(self):
        return self.__nombreCliente

    @nombre.setter
    def nombre(self, nombre):

        if len(nombre.strip()) < 3:
            raise ClienteError("Nombre inválido")

        if not nombre.replace(" ", "").isalpha():
            raise ClienteError("El nombre solo debe contener letras")

        self.__nombreCliente = nombre

    @property
    def telefono(self):
        return self.__telefonoCliente

    @telefono.setter
    def telefono(self, telefono):
    
        telefono_limpio= telefono.replace("-", "")

        if not telefono_limpio.isdigit():
            raise ClienteError("Teléfono inválido")
        
        if len(telefono_limpio) < 7:
            raise ClienteError("Número telefonico muy corto")
        
        self.__telefonoCliente = telefono

class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, *args):
        pass

    @abstractmethod
    def descripcion(self):
        pass

#  SERVICIOS
# se crean clases derivadas de la clase abstracta Servicio para representar servicios específicos que ofrece la empresa, implementando los métodos abstractos para calcular costos y describir el servicio, además de incluir validaciones específicas para cada tipo de servicio 
class ReservaSala(Servicio):
    def __init__(self, horas, disponible= True):
        super().__init__("Reserva de Sala")
    
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        
        self.horas = horas
        self.disponible = disponible
   
    def calcular_costo(self, descuento=0):
        costo = self.horas * 50000
        return costo - (costo * descuento)

    def descripcion(self):
      return f"sala por{self.horas} horas"

class AlquilerEquipo(Servicio):
    def __init__(self, dias):
        super().__init__("Alquiler de Equipo")
        if dias <= 0:
            raise ServicioError("Días inválidos")
        self.dias = dias

    def calcular_costo(self, impuesto=0):
        costo = self.dias * 30000
        return costo + (costo * impuesto)

    def descripcion(self):
        return f"Equipo por {self.dias} días"
# Valores de prueba 
cliente1 = Cliente("123456789", "Juan Perez", "555-1234")
print(f"Documento: {cliente1.documento}")  # Imprime: 123456789
print(f"Nombre: {cliente1.nombre}")  # Imprime: Juan Perez
print(f"Teléfono: {cliente1.telefono}")  # Imprime: 555-1234
# Ejemplo de modificación de un atributo utilizando el setter
cliente1.documento = "987654321"
print(f"Documento modificado: {cliente1.documento}")  # Imprime: 987654321
# No es posible acceder directamente a los atributos privados desde fuera de la clase
# Demostración del manejo de excepción de atributo
try:
    print(cliente1.__documentoCliente) # Se intenta acceder a un atributo privado directamente
except AttributeError:
    print(f"Error de atributo: El atributo no existe o no es accesible.") # Imprime el mensaje de error de atributo. También es necesario manejar la excepción y registrarlo en el archivo de logs a futuro


import logging

logging.basicConfig(filename="logs.txt", level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

# excepciones personalizadas
class ReservaError(Exception):
    pass

class ClienteError(Exception):
    pass

class ServicioError(Exception):
    pass


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        try:

            if not isinstance(cliente, Cliente):
                raise ReservaError("Cliente inválido")

            if not isinstance(servicio, Servicio):
                raise ReservaError("Servicio inválido")

            if duracion <= 0:
                raise ReservaError("La duración debe ser mayor a cero")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "pendiente"

            logging.info("Reserva creada correctamente")

        except ReservaError as e:
            logging.error(f"Error en reserva: {e}")
            raise

        finally:
            logging.info("Proceso de creación de reserva finalizado")

    def confirmar(self):

        try:

            if self.estado == "cancelada":
                raise ReservaError("No se puede confirmar una reserva cancelada")

            self.estado = "confirmada"

        except ReservaError as e:
            logging.error(f"Error confirmando reserva: {e}")
            raise

    def cancelar(self):

        try:

            if self.estado == "confirmada":
                raise ReservaError("No se puede cancelar una reserva confirmada")

            self.estado = "cancelada"

        except ReservaError as e:
            logging.error(f"Error cancelando reserva: {e}")
            raise

    def calcular_total(self):

        try:

            total = self.servicio.calcular_costo()

            if total < 0:
                raise ReservaError("Total inconsistente")

            return total

        except Exception as e:

            logging.error(f"Error calculando total: {e}")

            raise ReservaError(
                "No fue posible calcular el total") from e

    def mostrar(self):

        return (
            f"{self.cliente.nombre} | "
            f"{self.servicio.descripcion()} | "
            f"{self.estado}")
            
#Creacion del clase de servisio (servisio_al_cliente )
class ServicioAlCliente(Servicio):
    def __init__(self, nombre, costo_fijo):
        super().__init__(nombre)
        if costo_fijo < 0:
            raise ServicioError("Costo fijo inválido")
        self.costo_fijo = costo_fijo

    def calcular_costo(self, *args):
        return self.costo_fijo

    def descripcion(self):
        return f"Servicio al cliente: {self.nombre}"
    
clientes = []
servicios = []
reservas = []

print ("INICIO DE LA SIMULACIÓN")

#Caso 1: CLiente Valido
try:
    c1 = Cliente("123456", "juan", "1234567")
    #se llama a la función de validación para verificar que el cliente cumple con los requisitos antes de agregarlo a la lista de clientes, si el cliente es válido se agrega a la lista y se imprime un mensaje de éxito, en caso contrario se captura la excepción y se imprime un mensaje de error
    validar_cliente(c1)
    clientes.append(c1)
    print("caso 1 ok")
except Exception as e:
    print("caso 1 error")

# Caso 2: cliente invalido (nombre corto)
try:
    c2 = Cliente("789456", "jo", "1234567")
    #se llama a la función de validación para verificar que el cliente cumple con los requisitos antes de agregarlo a la lista de clientes, si el cliente es válido se agrega a la lista y se imprime un mensaje de éxito, en caso contrario se captura la excepción y se imprime un mensaje de error
    validar_cliente(c2)
    clientes.append(c2)
    print("caso 2 ok")
except:
    print("caso 2 error")

# Caso 3: servicio valido
#se intenta crear una instancia de ReservaSala con una duración válida, si la creación es exitosa se agrega el servicio a la lista de servicios y se imprime un mensaje de éxito, en caso de que ocurra un error durante la creación del servicio, se captura la excepción y se registra un mensaje de error en el archivo de logs
try:
    s1 = ReservaSala(2)
    
except ServicioError as e:

      logging.error(f"Error creando servicio: {e}")

else:
    servicios.append(s1)
    print("Servicio agregado correctamente")

# Caso 4: servicio invalido
try:
    s2 = ReservaSala(-5)
    servicios.append(s2)
    print("caso 4 ok")
except Exception as e:
    print("caso 4 error")

# Caso 5: reserva valida
try:
    r1 = Reserva(c1, s1, 2)
   
except ReservaError as e:

    print(e)

finally:  
    
     print("Proceso de reserva terminado")

# Caso 6: reserva con duracion mala
try:
    r2 = Reserva(c1, s1, -1)
    reservas.append(r2)
    print("caso 6 ok")
except Exception as e:
    print("caso 6 error")
# CASO 7: servicio equipo valido
try:
    s3 = AlquilerEquipo(3)
    servicios.append(s3)
    print("caso 7 ok")
except Exception as e:
    print("caso 7 error")

# CASO 8: reserva con servicio equipo
try:
    r3 = Reserva(c1, s3, 3)
    r3.confirmar()
    reservas.append(r3)
    print("caso 8 ok:", r3.mostrar())
except Exception as e:
    print("caso 8 error")

# CASO 9: cliente con documento invalido
try:
    c3 = Cliente("abc", "pedro", "1234567")
    validar_cliente(c3)
    clientes.append(c3)
    print("caso 9 ok")
except Exception as e:
    print("caso 9 error")

# CASO 10: servicio al cliente
#se intenta crear una instancia de ServicioAlCliente con un costo fijo válido, si la creación es exitosa se agrega el servicio a la lista de servicios y se imprime un mensaje de éxito, en caso de que ocurra un error durante la creación del servicio, se captura la excepción y se registra un mensaje de error en el archivo de logs
try:
    s4 = ServicioAlCliente("asesoria", 100000)
    servicios.append(s4)
    r4 = Reserva(c1, s4, 1)
    r4.confirmar()
    reservas.append(r4)
    print("caso 10 ok:", r4.mostrar())
except Exception as e:
    print("caso 10 error")

print("FIN SIMULACION")