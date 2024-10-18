from abc import ABC, abstractmethod

class EditorTextoBase(ABC):
    @abstractmethod
    def aplicar_formato(self):
        pass