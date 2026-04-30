#Descripción del ejercicio 
#Grupo-411
#Ejercicio 1: Sistema Integral de Gestión de Clientes, Servicios y
#Reservas
#En un equipo conformado por cinco (5) estudiantes, deberán desarrollar
#un sistema integral orientado a objetos, sin uso de bases de datos,
#capaz de gestionar clientes, servicios y reservas para una empresa
#llamada Software FJ que ofrece varios tipos de servicios (reservas de
#salas, alquiler de equipos y asesorías especializadas). El objetivo de esta
#tarea es construir una aplicación estable, modular y extensible que
#implemente de forma rigurosa los principios de abstracción, herencia,
#polimorfismo, encapsulación y manejo avanzado de excepciones,
#garantizando que el sistema siga funcionando aun cuando se presenten
#errores durante su ejecución.
#El sistema debe incluir clases abstractas, clases derivadas, métodos
#sobrecargados, manejo de listas internas y validaciones estrictas,
#demostrando un diseño orientado a objetos completamente funcional. La
#información no debe almacenarse en bases de datos; toda la gestión
#debe hacerse mediante objetos, listas y manejo de archivos únicamente
#para el registro de eventos y errores.
#Como parte esencial de la tarea, el sistema deberá incorporar manejo
#robusto de excepciones, incluyendo excepciones personalizadas, uso
#de bloques try/except, try/except/else, try/except/finally, y
#encadenamiento de excepciones. Cada error detectado debe registrarse
#en un archivo de logs, manteniendo la aplicación activa y estable en
#todo momento. El sistema debe ser capaz de manejar errores
#provenientes de datos inválidos, parámetros faltantes, operaciones no
#permitidas, intentos de reserva incorrectos, servicios no disponibles,
#cálculos inconsistentes y cualquier otra situación que pueda
#comprometer la operación normal de la aplicación.
#El trabajo debe basarse en una arquitectura orientada a objetos,
#incluyendo al menos:
#• Una clase abstracta que represente entidades generales del
#sistema.
#• Una clase Cliente con validaciones robustas y encapsulación de
#datos personales.
#• Una clase abstracta Servicio y al menos tres servicios
#especializados que hereden de ella, implementando polimorfismo y
#métodos sobrescritos para calcular costos, describir servicios y
#validar parámetros.
#• Una clase Reserva que integre cliente, servicio, duración y estado,
#e implemente confirmación, cancelación y procesamiento con
#manejo de excepciones.
#• Métodos sobrecargados (por ejemplo, diferentes variantes del
#cálculo de costos con impuestos, descuentos o parámetros
#opcionales).
#• Un archivo de logs donde se registren todos los errores y eventos
#relevantes.
#El sistema, sin utilizar ningún motor de base de datos, debe simular al
#menos 10 operaciones completas, incluyendo registros válidos e
#inválidos de clientes, creación correcta e incorrecta de servicios, y
#reservas exitosas y fallidas, demostrando la capacidad del programa
#para continuar funcionando ante errores graves y manejar excepciones
#de manera controlada y profesional.
#El equipo debe entregar un único proyecto completamente funcional,
#organizado, documentado y capaz de ejecutarse sin interrupciones,
#demostrando la correcta aplicación de la programación orientada a
#objetos y el manejo avanzado de excepciones en un entorno sin base de
#datos.

# Clase cliente que encapsula los datos personales de un cliente
class Cliente():
    # Constructor de la clase Cliente que inicializa los atributos del cliente
    def __init__(self, documento, nombre, telefono):
        self.__documentoCliente = documento
        self.__nombreCliente = nombre
        self.__telefonoCliente = telefono
    # Métodos getter y setter para acceder y modificar los atributos del cliente desde fuera de la clase
    @property
    def documento(self):
        return self.__documentoCliente
    
    @property
    def nombre(self):
        return self.__nombreCliente
    
    @property
    def telefono(self):
        return self.__telefonoCliente
    
    @documento.setter
    def documento(self, documento):
        self.__documentoCliente = documento  
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombreCliente = nombre
    
    @telefono.setter
    def telefono(self, telefono):
        self.__telefonoCliente = telefono
        
if validar_cliente(cliente):
    try:
        if not cliente.documento.isdigit():
            raise ClienteError("Documento inválido")
        if len(cliente.nombre) < 3:
            raise ClienteError("Nombre inválido")
        if len(cliente.telefono) < 7:
            raise ClienteError("Teléfono inválido")
    except Exception as e:
        logging.error(f"Error en validación de cliente: {e}")
        raise

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
class ReservaSala(Servicio):
    def __init__(self, horas):
        super().__init__("Reserva de Sala")
        if horas <= 0:
            raise ServicioError("Horas inválidas")
        self.horas = horas

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

#Parte de Juan Pablo
class reserva:
    def __init__(self, cliente, servicio, duracion):
        try:
            if duracion <= 0:
                raise Exception("duracion mala")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "pendiente"

        except Exception as e:
            logging.error("error en reserva " + str(e))
            print("error creando reserva")

    def confirmar(self):
        self.estado = "confirmada"

    def cancelar(self):
        self.estado = "cancelada"

    def calcular_total(self):
        try:
            return self.servicio.calcular_costo()
        except Exception as e:
            logging.error("error calculo " + str(e))
            print("error en calculo")
            return 0

    def mostrar(self):
        try:
            return self.cliente.nombre + " - " + self.servicio.descripcion() + " - " + self.estado
        except Exception as e:
            logging.error("error mostrando " + str(e))
            return "no se pudo mostrar"


