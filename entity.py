# ============================================================
# CLASE ABSTRACTA DE ENTIDADES
# ============================================================
from abc import ABC, abstractmethod

class Entidad(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def __str__(self):
        pass
