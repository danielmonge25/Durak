from abc import ABC, abstractmethod

class Game(ABC):
  
  @abstractmethod
  def __init__(self) -> None:
    self.reglas = ""
    
  #esqueleto del juego
  def play(self) -> None:
    pass


  @abstractmethod
  def next_turn(self) -> None:
    pass
    
  @abstractmethod
  def set_rules(self) -> None:
    pass
    

  @abstractmethod
  def get_state(self) -> None:
    pass

  @abstractmethod
  def get_card(self) -> None:
    pass

  @abstractmethod
  def end(self) -> None:
    pass

