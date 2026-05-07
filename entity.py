#Se crea clase Entidad, la cual es la clase padre de todas las entidades 
#se esporta las herraminetas para la clase abtracta
from abc import ABC, abstractmethod

# ============================================================
# CLASE ABSTRACTA DE ENTIDADES
# ============================================================

class Entidad(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def __str__(self):
        pass
