#------------------------------------------------------------------------------------------------------------------------
# Importación de la función abstractmethod para definir métodos abstractos en la clase Servicio.
#------------------------------------------------------------------------------------------------------------------------
from abc import abstractmethod 
#------------------------------------------------------------------------------------------------------------------------
# Importacion de la clase Entidad para que cliente pueda heredar de ella
#------------------------------------------------------------------------------------------------------------------------
from entity import Entidad
#------------------------------------------------------------------------------------------------------------------------
# Importación del módulo de excepciones personalizadas para manejar errores específicos relacionados con los servicios.
#------------------------------------------------------------------------------------------------------------------------
import excepciones

# =========================================================================================================
# CLASE ABSTRACTA SERVICIO
# =========================================================================================================

class Servicio(Entidad):
    """
    Clase Servicio que representa un servicio ofrecido por el sistema.
    Es una clase abstracta que define la estructura básica de un servicio, incluyendo su nombre, precio y métodos abstractos 
    para calcular el costo y describir el servicio.    
    """
    def __init__(self, nombre, precio):
        super().__init__()
        self.nombre = nombre
        self.precio = precio
        if precio < 0:
            raise excepciones.ServicioError("El precio debe ser mayor o igual a 0")
        
    @abstractmethod
    def calcular_costo(self):
        # Método abstracto para calcular el costo del servicio.
        pass

    @abstractmethod
    def descripcion(self):
        # Método abstracto para describir el servicio.
        pass
    
    def __str__(self):
            return f"{self.nombre} - {self.precio} pesos"
    
    __repr__ = __str__
    
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # Método estático para crear un servicio a partir de la selección del usuario, solicitando los detalles necesarios para cada tipo de servicio.
    # --------------------------------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def crear_servicio():
        try:
            print("===========================================")
            print("Servicios de Software FJ:")
            print("===========================================")
            print("1. Reservar Sala")
            print("2. Alquilar Equipo")
            print("3. Servicio Especial")
            opcion = int(input("- Seleccione el número de la opción: "))
            if opcion == 1:
                tiempo = int(input("- Ingrese la duración de la reserva en horas: "))
                return ReservaSala(tiempo)
            elif opcion == 2:
                equipo = input("- Ingrese el nombre del equipo a alquilar: ")
                dias = int(input("- Ingrese la cantidad de días para el alquiler: "))
                return AlquilerEquipo(equipo, dias)
            elif opcion == 3:
                nombre = input("- Ingrese el nombre del servicio especial: ")
                costo_fijo = float(input("- Ingrese el costo fijo del servicio especial: "))
                return ServiciosEspeciales(nombre, costo_fijo)
            else:
                raise ValueError("Opción inválida para crear servicio")
        
        except ValueError as e:
                raise ValueError(f"Entrada inválida. Debe ingresar números correctos. Error: {e}")


# ============================================================
# CLASES DERIVADAS DE SERVICIO
# ============================================================

class ReservaSala(Servicio):
    """
    Clase ReservaSala que representa un servicio de reserva de sala.
    Hereda de la clase Servicio y proporciona una implementación específica para calcular 
    el costo basado en la duración de la reserva, así como una descripción del servicio.  
    """
    def __init__(self, tiempo):
        super().__init__("Reserva de Sala", 50000) # Se llama al constructor de la clase base para establecer el nombre y precio del servicio.
        if tiempo <= 0:
            raise excepciones.ServicioError("La tiempo de duracion de la reserva debe ser mayor que cero.")
        self.tiempo = tiempo

#Sobreescritura de metodo calcular_costo abstracto 
    def calcular_costo(self, descuento=0): # El método calcular_costo ahora incluye un parámetro opcional para aplicar un descuento al costo total de la reserva.
        costo = self.tiempo * self.precio
        return costo - (costo * descuento/ 100)

#Sobreescritura de metodo descripcion abstracto
    def descripcion(self):
      return f"Reserva de sala por {self.tiempo} horas"

class AlquilerEquipo(Servicio):
    """
    Clase AlquilerEquipo que representa un servicio de alquiler de equipo.
    Hereda de la clase Servicio y proporciona una implementación específica para calcular 
    el costo basado en la cantidad de días para el alquiler, así como una descripción del servicio.  
    """
    def __init__(self, equipo, dias):
        super().__init__("Alquiler de Equipo", 30000) # Se llama al constructor de la clase base para establecer el nombre y precio del servicio.
        if equipo.strip() == "":
            raise excepciones.ServicioError("El nombre del equipo no puede estar vacío.")
        self.equipo = equipo
        if dias <= 0:
            raise excepciones.ServicioError("La cantidad de días para el alquiler debe ser mayor que cero.")
        self.dias = dias

    def calcular_costo(self, impuesto=0): # El método calcular_costo ahora incluye un parámetro opcional para aplicar un impuesto al costo total del alquiler.
        costo = self.dias * self.precio
        return costo + (costo * impuesto/ 100)
    
    def descripcion(self):
        return f"Alquiler de equipo: {self.equipo} por {self.dias} días"
    
class ServiciosEspeciales(Servicio):
    """
    Clase ServiciosEspeciales que representa un servicio especial.
    Hereda de la clase Servicio y proporciona una implementación específica para calcular 
    el costo basado en un valor fijo, así como una descripción del servicio.  
    """
    def __init__(self, nombre, costo_fijo):
        super().__init__(nombre, 0)  # Precio inicial en 0, ya que el costo es fijo
        if costo_fijo < 0:
            raise excepciones.ServicioError("El costo fijo debe ser mayor o igual a 0.")
        self.costo_fijo = costo_fijo

    def calcular_costo(self):
        return self.costo_fijo

    def descripcion(self):
        return f"Servicio especial: {self.nombre} | Costo: {self.costo_fijo} pesos"
    