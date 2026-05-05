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
        
#deinicon de servicio error para manejar errores específicos relacionados con los servicios ofrecidos por la empresa
class ServicioError(Exception):
    pass

#definicion de excepciones personalizadas para el manejo de errores específicos del sistema
class ClienteError(Exception):
    pass
def validar_cliente(cliente):
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

#creacion de clase astrapta para representar servicios generales del sistema, con métodos abstractos que deben ser implementados por las clases derivadas
from abc import ABC, abstractmethod

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

# Parte de Juan Pablo
# ahora paso a trabajar la parte de reservas con manejo de errores y validaciones

import logging
logging.basicConfig(filename="logs.txt", level=logging.ERROR)

# excepciones personalizadas
class ReservaError(Exception):
    pass

class ClienteError(Exception):
    pass

class ServicioError(Exception):
    pass


class reserva:
    def __init__(self, cliente, servicio, duracion):
        try:
            if duracion <= 0:
                raise ReservaError("duracion mala")

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
#He analizado el codigo en VS y aparecen errores en amarillo verifiquen lo que hemos hecho, hago más???

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
    

#Parte 2 de Juan Pablo
#Pasaré a hacer la simulación el sistema (10 casos)

clientes = []
servicios = []
reservas = []

print ("INICIO DE LA SIMULACIÓN")

#Caso 1: CLiente Valido
try:
    c1 = Cliente("123456", "juan", "1234567")
    validar_cliente(c1)
    clientes.append(c1)
    print("caso 1 ok")
except:
    print("caso 1 error")

# Caso 2: cliente invalido (nombre corto)
try:
    c2 = Cliente("789456", "jo", "1234567")
    validar_cliente(c2)
    clientes.append(c2)
    print("caso 2 ok")
except:
    print("caso 2 error")

# Caso 3: servicio valido
try:
    s1 = ReservaSala(2)
    servicios.append(s1)
    print("caso 3 ok")
except:
    print("caso 3 error")

# Caso 4: servicio invalido
try:
    s2 = ReservaSala(-5)
    servicios.append(s2)
    print("caso 4 ok")
except:
    print("caso 4 error")

# Caso 5: reserva valida
try:
    r1 = reserva(c1, s1, 2)
    r1.confirmar()
    reservas.append(r1)
    print("caso 5 ok:", r1.mostrar())
except:
    print("caso 5 error")

# Caso 6: reserva con duracion mala
try:
    r2 = reserva(c1, s1, -1)
    reservas.append(r2)
    print("caso 6 ok")
except:
    print("caso 6 error")
# CASO 7: servicio equipo valido
try:
    s3 = AlquilerEquipo(3)
    servicios.append(s3)
    print("caso 7 ok")
except:
    print("caso 7 error")

# CASO 8: reserva con servicio equipo
try:
    r3 = reserva(c1, s3, 3)
    r3.confirmar()
    reservas.append(r3)
    print("caso 8 ok:", r3.mostrar())
except:
    print("caso 8 error")

# CASO 9: cliente con documento invalido
try:
    c3 = Cliente("abc", "pedro", "1234567")
    validar_cliente(c3)
    clientes.append(c3)
    print("caso 9 ok")
except:
    print("caso 9 error")

# CASO 10: servicio al cliente
try:
    s4 = ServicioAlCliente("asesoria", 100000)
    servicios.append(s4)
    r4 = reserva(c1, s4, 1)
    r4.confirmar()
    reservas.append(r4)
    print("caso 10 ok:", r4.mostrar())
except:
    print("caso 10 error")

print("FIN SIMULACION")

#Dividan sus partes me aparece que hice todo yo xd -----> Con todo respeto compañero la unicaforma que ocura eso es que remplases lo anterior mente escrito o copies y pegues el codigo de forma externa a las actualizaciones de los commits de otro archivo o proyecto y lo subas a git en ves de solo añadir lo nuevo.
#Si guiente a eso compañero no hay necesidad completa de estar escribiendo el nombre ya que como dice la guia de apredisaje y la rubrica mediante el uso de los commit se indica que deben de ir comentados el primero con el nombre del partisipante y los demas con las modifacsiones areglos o exepciones que se hicieron en el codigo, lo importante es que el codigo este completo y funcional, y que se hayan cumplido los requisitos del ejercicio.
#Siguente a eso el repositorio git hay un partado que informa la partisipasion genetal y espesifiaca de todos los partispnates al igual que la cantidad de commit y lineas de codigo escritas o modicadas propias o de otros compañeros
#Ademas el comentar o realisar charlas en el codigo es una mala practica para eso existe el foro de dicucion y los medios de comunicasion dispuestos por la unversidad 
#Los mensaje presentes seran borrados antes de la entrega y solo se dejaran los comentarios que comenten el funcionamineto o guia del sistema fometando un codigo estruturalmente limpio de comnetarios inecesarios
# Si ya tienen una parte buena en partisipacion agradesco esperes a que los copañeros con menor aporte agregen su parte.
#Actual mente el codigo tiene pocos puntos para añadir por lo que dejareunas indicasiones de lo que aun falta para quieres aun no han partisipado mucho
#Ademas de comentar en el documento trabajo el error de copiar y pegar que te pudo aver pasado y por lo cual puede parecer que reaalisaste todo, como inidacion te recominedo el solo modifacar aquello con errores o malas practicas y mantener tus añadidos comentados en el commit 
# Comprendo que esto le pude pasar a cualquiera por lo que es importante estar anteto a los cambios que se hacen en el codigo y revisar los commits para asegurarse de que se esta añadiendo lo nuevo y no se esta remplazando lo anterior sin necesidad de cambio real o modificasion, ademas de mantener una buena comunicacion con el equipo para evitar este tipo de confusiones.
#los invito a realisar comentarios de este tipo en el foro
#Recalco el dia antes de la entrega yo personalmente borrare los comentarios inecesarios que no aporten al codigo u a su desarrollo ademas de avisar y mandar evidencia de la modifacon al foro como contacia de que no se borro nada que fuera nesesario.

#Cosas para mejorar o añadir guia para quienes no tienen mucha partisioacion : se detecta repeticion de exepciones, hay que coregir el implementado de la clase reserve, implemetacion de execiones mas un poquioto mas avansadas, mejorar la validasion de procesos dentro de la clase cliente (para aquellos cue no han partisipado mucho)