# Importación de módulos necesarios para la implementación de la clase Servicio y sus derivados, 
# así como para el manejo de excepciones y la interacción con la clase Cliente.
import cliente
import excepciones

#Clase abstracta Servicio, con métodos abstractos que deben ser implementados por las clases derivadas
from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, *args):
        # Método abstracto para calcular el costo del servicio.
        pass

    @abstractmethod
    def descripcion(self):
        # Método abstracto para describir el servicio.
        pass

#  SERVICIOS 
# Se crean clases derivadas de la clase abstracta Servicio para representar servicios específicos que ofrece la empresa.
class ReservaSala(Servicio):
    def __init__(self, horas):
        super().__init__("Reserva de Sala")
        if horas <= 0:
            raise excepciones.ServicioError("Horas inválidas")
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
            raise excepciones.ServicioError("Días inválidos")
        self.dias = dias

    def calcular_costo(self, impuesto=0):
        costo = self.dias * 30000
        return costo + (costo * impuesto)

    def descripcion(self):
        return f"Equipo por {self.dias} días"
    
class ServicioAlCliente(Servicio):
    def __init__(self, nombre, costo_fijo):
        super().__init__(nombre)
        if costo_fijo < 0:
            raise excepciones.ServicioError("Costo fijo inválido")
        self.costo_fijo = costo_fijo

    def calcular_costo(self, *args):
        return self.costo_fijo

    def descripcion(self):
        return f"Servicio al cliente: {self.nombre}"
    
# Valores de prueba 
cliente1 = cliente.Cliente("123456789", "Juan Perez", "555-1234")
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