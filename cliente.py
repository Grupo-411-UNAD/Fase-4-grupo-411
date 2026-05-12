# --------------------------------------------------------------------------------------------------------------------------------------------
# Importacion de la clase Entidad para que cliente pueda heredar de ella
# --------------------------------------------------------------------------------------------------------------------------------------------
from entity import Entidad
# --------------------------------------------------------------------------------------------------------------------------------------------
# Importacion de módulos necesarios para la implementación de la clase Cliente, así como para el manejo de excepciones
# --------------------------------------------------------------------------------------------------------------------------------------------
import excepciones
# --------------------------------------------------------------------------------------------------------------------------------------------
# Clase cliente que encapsula los datos personales de un cliente
# --------------------------------------------------------------------------------------------------------------------------------------------
class Cliente(Entidad):
    def __init__(self, nombre, documento, telefono):

        super().__init__()

        if not nombre.replace(" ", "").isalpha():
            raise excepciones.ClienteError(
            "El nombre solo debe contener letras"
            )

        if (
            not documento.isdigit()
            or len(documento) < 6
            or len(documento) > 12
            or documento[0] == '0'
            ):
            raise excepciones.ClienteError(
            "Documento inválido"
            )

        if (
            not telefono.isdigit()
            or len(telefono) < 7
            or len(telefono) > 15
            or telefono[0] == '0'
            ):
            raise excepciones.ClienteError(
                "Teléfono inválido"
            )
# Atributos encapsulados con doble guion bajo para proteger los datos
        self.__nombreCliente = nombre
        self.__documentoCliente = documento
        self.__telefonoCliente = telefono
        
    def __str__(self):
            return f"{self.nombre} - {self.documento} - {self.telefono}"

    __repr__ = __str__
    
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Métodos getter y setter para acceder y modificar los atributos del cliente desde fuera de la clase y encapsular los datos para protegerlos de accesos no autorizados.
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # nombre
    @property
    def nombre(self):
        return self.__nombreCliente

    @nombre.setter
    def nombre(self, nombre):
        self.__nombreCliente = nombre

    # documento
    @property
    def documento(self):
        return self.__documentoCliente

    @documento.setter
    def documento(self, documento):
        self.__documentoCliente = documento

    # teléfono
    @property
    def telefono(self):
        return self.__telefonoCliente

    @telefono.setter
    def telefono(self, telefono):
        self.__telefonoCliente = telefono

    # ------------------------------------------------------------------------------------------------------------------------------------------
    # Método para mostrar los datos del cliente.
    # ------------------------------------------------------------------------------------------------------------------------------------------
    def mostrar_datos(self): 
            print(f"\n Cliente: {self.__nombreCliente} | Documento: {self.__documentoCliente} | Teléfono: {self.__telefonoCliente} \n")
            
    # ============================================================================================================================================
    # FUNCION REGISTRAR CLIENTE
    # ============================================================================================================================================
    
    @staticmethod
    def registrar_cliente():
        try:

            nombre = input("\n -Ingrese el nombre del cliente:  ")

            if not nombre.replace(" ", "").isalpha():
                raise excepciones.ClienteError("El nombre solo debe contener letras")

            documento = input("\n -Ingrese el documento del cliente:  ")

            if (
                not documento.isdigit()
                or len(documento) < 6
                or len(documento) > 12
                or documento[0] == '0'
            ):
                raise excepciones.ClienteError("Documento inválido")

            telefono = input("\n -Ingrese el teléfono del cliente:  ")

            if (
                not telefono.isdigit()
                or len(telefono) < 7
                or len(telefono) > 15
                or telefono[0] == '0'
            ):
                raise excepciones.ClienteError("Teléfono inválido")

            return Cliente(nombre, documento, telefono)

        except Exception as e:

            excepciones.registrar_log(f"Error registrando cliente: {e}")
            raise