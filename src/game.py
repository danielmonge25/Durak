'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
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
  def verify_turn(self) -> None:
    """
      Metodo abstracto que verifica si los jugadores tienen cartas

      Esta funcion no retorna nada
    """

    pass
  
  @abstractmethod
  def next_round(self) -> None:
    """
      Metodo abstracto que prepara el juego para la siguiente ronda

      Esta funcion no retorna nada
    """

    pass
  
  @abstractmethod
  def sum_score(self) -> None:
    """
      Metodo abstracto que suma el puntaje del jugador 1

      Esta funcion no retorna nada
    """

    pass
  
  @abstractmethod
  def reset_values(self) -> None:
    """
      Metodo abstracto que reinicia los numeros de las cartas que ambos jugadores usaron

      Esta funcion no retorna nada
    """

    pass

  @abstractmethod
  def verify_number(self) -> None:
    """
      Metodo abstracto que verifica si la carta que jugo el defensor es mayor a la del atacante


      Esta funcion no retorna nada
    """

    pass

  @abstractmethod
  def verify_suit(self) -> None:
    """
      Metodo abstracto que verifica si la carta que jugo el defensor es del mismo tipo que la del atacante o de la carta especial

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
  def save_game(self) -> None:
    """
      Metodo abstracto que guarda los datos de la partida

      Esta funcion no retorna nada
    """

    pass
  
  @abstractmethod
  def load_game(self) -> None:
    """
      Metodo abstracto que carga los datos de la partida

      Esta funcion no retorna nada
    """

    pass

  @abstractmethod
  def get_special_card(self) -> None:
    """
      Metodo abstracto que devuelve la carta especial del juego
    """

    pass

  @abstractmethod
  def get_suit(self) -> None:
    """
      Metodo abstracto que devuelve el tipo de la carta que el jugador va a jugar
    """

    pass

  @abstractmethod
  def set_deck(self) -> None:
    """
      Metodo abstracto que establece el deck del juego
    """

    pass

  @abstractmethod
  def set_special_card(self) -> None:
    """
      Metodo abstracto que establece la carta especial del juego
    """

    pass

  @abstractmethod
  def get_card_name(self) -> None:
    """
      Metodo abstracto que obtiene el nombre de una carta
    """

    pass