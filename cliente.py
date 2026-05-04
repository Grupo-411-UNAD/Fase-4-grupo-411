# Importación de módulos necesarios para la implementación de la clase Cliente, así como para el manejo de excepciones
import excepciones

# Clase cliente que encapsula los datos personales de un cliente
class Cliente():
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
        
    def validar_cliente(cliente):
        try:
            if not cliente.documento.isdigit():
                raise excepciones.ClienteError("Documento inválido")
            if len(cliente.nombre) < 3:
                raise excepciones.ClienteError("Nombre inválido")
            if len(cliente.telefono) < 7:
                raise excepciones.ClienteError("Teléfono inválido")
        except Exception as e:
            excepciones.logging.error(f"Error en validación de cliente: {e}")
            raise excepciones.ClienteError("Error en validación de cliente")

