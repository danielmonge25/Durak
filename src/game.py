'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel MOnge, Alejandro Sanchez, Andre Villegas
'''

from abc import ABC, abstractmethod

class Game(ABC):
  
  @abstractmethod
  def __init__(self) -> None:
    """
      Constructor de la clase abstracta Game

      Esta funcion no retorna nada
    """

    self.reglas = ""
    
  #esqueleto del juego
  @abstractmethod
  def play(self) -> None:
    """
      Metodo abstracto que comienza el juego

      Esta funcion no retorna nada
    """

    pass

  @abstractmethod
  def draw(self) -> None:
    """
      Metodo abstracto que reparte las cartas

      Esta funcion no retorna nada
    """

    pass

  @abstractmethod
  def next_turn(self) -> None:
    """
      Metodo abstracto que indica el cambio de turno

      Esta funcion no retorna nada
    """

    pass
    
  @abstractmethod
  def set_rules(self) -> None:
    """
      Metodo abstracto que establece las reglas del juego

      Esta funcion no retorna nada
    """

    pass
    

  @abstractmethod
  def get_state(self) -> None:
    """
      Metodo abstracto que establece el estado del juego

      Esta funcion no retorna nada
    """

    pass

  @abstractmethod
  def get_card(self) -> None:
    """
      Metodo abstracto que da una carta a un jugador

      Esta funcion no retorna nada
    """

    pass

  @abstractmethod
  def end(self) -> None:
    """
      Metodo abstracto que indica el fin del juego

      Esta funcion no retorna nada
    """

    pass

