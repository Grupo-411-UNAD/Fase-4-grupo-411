# Importación de módulos necesarios para la implementación de la clase Servicio y sus derivados, 
# así como para el manejo de excepciones y la interacción con la clase Cliente.
import excepciones

# ============================================================
# CLASE ABSTRACTA SERVICIO
# ============================================================

from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio):
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
        
        except ValueError:
                raise ValueError("Entrada inválida. Debe ingresar números correctos.")


# ============================================================
# CLASES DERIVADAS DE SERVICIO
# ============================================================

class ReservaSala(Servicio):
    def __init__(self, tiempo):
        super().__init__("Reserva de Sala", 50000) # Se llama al constructor de la clase base para establecer el nombre y precio del servicio.
        if tiempo <= 0:
            raise excepciones.ServicioError("La tiempo de duracion de la reserva debe ser mayor que cero.")
        self.tiempo = tiempo

    def calcular_costo(self, descuento=0): # El método calcular_costo ahora incluye un parámetro opcional para aplicar un descuento al costo total de la reserva.
        costo = self.tiempo * self.precio
        return costo - (costo * descuento/ 100)

    def descripcion(self):
      return f"Reserva de sala por {self.tiempo} horas"

class AlquilerEquipo(Servicio):
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
    def __init__(self, nombre, costo_fijo):
        super().__init__(nombre, 0)  # Precio inicial en 0, ya que el costo es fijo
        if costo_fijo < 0:
            raise excepciones.ServicioError("El costo fijo debe ser mayor o igual a 0.")
        self.costo_fijo = costo_fijo

    def calcular_costo(self):
        return self.costo_fijo

    def descripcion(self):
        return f"Servicio especial: {self.nombre} | Costo: {self.costo_fijo} pesos"
    
    
    
    
    
# Valores de prueba 
#cliente1 = cliente.Cliente("123456789", "Juan Perez", "555-1234")
#print(f"Documento: {cliente1.documento}")  # Imprime: 123456789
#print(f"Nombre: {cliente1.nombre}")  # Imprime: Juan Perez
#print(f"Teléfono: {cliente1.telefono}")  # Imprime: 555-1234
# Ejemplo de modificación de un atributo utilizando el setter
#cliente1.documento = "987654321"
#print(f"Documento modificado: {cliente1.documento}")  # Imprime: 987654321
# No es posible acceder directamente a los atributos privados desde fuera de la clase
# Demostración del manejo de excepción de atributo
#try:
#    print(cliente1.__documentoCliente) # Se intenta acceder a un atributo privado directamente
#except AttributeError:
#    print(f"Error de atributo: El atributo no existe o no es accesible.") # Imprime el mensaje de error de atributo. También es necesario manejar la excepción y registrarlo en el archivo de logs a futuro