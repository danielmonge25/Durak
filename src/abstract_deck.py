'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

from abc import ABC, abstractmethod

class Abstract_Deck(ABC):
    
    @abstractmethod
    def __init__(self) -> None:
        """
            Constructor de la clase abstracta Abstract_Deck

            Esta funcion no retorna nada
        """
        
        pass
    
    @abstractmethod
    def createDeck(self) -> None:
        """
            Metodo abstracto que crea el mazo para el juego

            Esta funcion no retorna nada
        """

        pass

    @abstractmethod
    def get_len_deck(self) -> None:
        """
            Metodo abstracto que devuelve el tamanyo del mazo
        """

        pass

    @abstractmethod
    def get_deck(self) -> None:
        """
            Metodo abstracto que devuelve el mazo del juego
        """

        pass
        
