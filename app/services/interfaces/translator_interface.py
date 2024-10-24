# app/services/interfaces/translator_interface.py
from abc import ABC, abstractmethod

class TranslatorInterface(ABC):
    @abstractmethod
    def translate(self, text: str) -> str:
        pass
