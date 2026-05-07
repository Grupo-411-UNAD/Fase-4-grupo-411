#se importa la clase entidad para que cliente pueda heredar de ella
from entity import Entidad

# Importación de módulos necesarios para la implementación de la clase Cliente, así como para el manejo de excepciones
import excepciones

# Clase cliente que encapsula los datos personales de un cliente
class Cliente(Entidad):
    def __init__(self, documento, nombre, telefono):
        super().__init__()
        self.__documentoCliente = documento
        self.__nombreCliente = nombre
        self.__telefonoCliente = telefono

    def __str__(self):
        return f"Cliente: {self.__nombreCliente}, Documento: {self.__documentoCliente}, Teléfono: {self.__telefonoCliente}"

    # Métodos getter y setter para acceder y modificar los atributos del cliente desde fuera de la clase
    
    # documento
    @property
    def documento(self):
        return self.__documentoCliente

    @documento.setter
    def documento(self, documento):
        if not documento.isdigit():
            raise excepciones.ClienteError("Documento inválido")
        self.__documentoCliente = documento

    # nombre
    @property
    def nombre(self):
        return self.__nombreCliente

    @nombre.setter
    def nombre(self, nombre):
        if not nombre.replace(" ", "").isalpha():
            raise excepciones.ClienteError("El nombre solo debe contener letras")
        self.__nombreCliente = nombre

    # teléfono
    @property
    def telefono(self):
        return self.__telefonoCliente

    @telefono.setter
    def telefono(self, telefono):
        if not telefono.isdigit() or len(telefono) < 7:
            raise excepciones.ClienteError("Teléfono inválido")
        self.__telefonoCliente = telefono
