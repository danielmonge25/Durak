'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

from abc import ABC, abstractmethod

class Abstract_Serializer(ABC):

    @abstractmethod
    def serialize_game(self) -> None:
        """
            Guarda la partida del juego

            Esta funcion no retorna nada
        """
        
        pass