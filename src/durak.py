'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

import csv
from game import Game

"""from visual import Visual
from deck import deck
from player import player"""

class durak(Game):
   def __init__(self, cards, player_one, player_two, visual):
      self.reglas = "El objetivo es descartar todas tus cartas antes que tus oponentes en diferentes rondas de ataque y defensa hasta que no hayan cartas en el mazo.\n Se juega con 36 cartas de la baraja inglesa, de menor a mayor valor: 6 7 8 9 10 J Q K A.\n Antes de empezar se coloca una carta boca arriba que indicará el palo de «triunfo». A cada jugador se le reparten 6 cartas. Si algún jugador tiene todas la cartas rojas, negras o 5 cartas del mismo palo, se vuelve a repartir. En cada ronda hay un defensor y un atacante. Empieza atacando el jugador que tiene la carta de triunfo más baja en su mano. El jugador a su izquierda es el defensor.\n El atacante juega una carta boca arriba sobre la mesa. El defensor debe responder con una carta superior del mismo palo o una carta del palo de triunfo para no perder la defensa. Se pueden realizar tantos ataques como cartas tiene el defensor hasta un máximo de 6. Para volver a atacar debe haber sobre la mesa una carta del mismo valor. Si un jugador no puede atacar más, pasará el turno al jugador de su izquierda.\n Final de la ronda \n La ronda finaliza cuando todos los jugadores han tenido oportunidad de atacar o se ha alcanzado el número máximo de ataques. Si el defensor ha tenido éxito, se descartarán todas las cartas de la mesa y será el primero en atacar en la siguiente ronda. Si ha fracasado, deberá robar todas las cartas de la mesa y perderá el turno de atacar en la siguiente ronda. Al acabar la ronda, todos los jugadores deberán robar del mazo hasta tener de nuevo 6 cartas, por orden primero los jugadores atacantes y por último el defensor.\n Final de la partida \n Gana el primer jugador que no tenga cartas y no haya cartas disponibles para robar. El resto de jugadores seguirán jugando para salvarse de ser el «durak»." 
      self.especial_card = ""
      self.score_player_one = 0
      self.score_player_two = 0

      self.cards = cards
      self.player_one = player_one
      self.player_two = player_two
      self.visual = visual

   def play(self):
      """
         Comienza el juego

         Esta funcion no retorna nada
      """
      self.player_one.set_player_name("Jugador 1")
      self.player_two.set_player_name("JUgador 2")
      # Creacion del mazo
      #cards = deck()
      self.cards.createDeck()

      # Creacion de los jugadores
      #player_one = player()
      #player_two = player()

      # Selecciona la carta especial
      self.especial_card = self.select_especial_card()

      # Reparte las cartas
      self.draw()

      #visual = Visual(self.reglas, cards.deck, player_one, player_two)

      # Establece las imagenes de las cartas
      if (self.player_one.get_size_hand() == 6):
         self.visual.config_image(self.player_one.get_hand(), self.player_two.get_hand(), self.especial_card)

      # Establece las reglas del juego
      self.visual.set_reglas(self.reglas)

      # Elige quien va de primero
      self.visual.pick_turn()

      # Muestra el juego
      self.visual.show_game()
   
   def next_round(self):
      self.sum_score()
      if (self.cards.get_len_deck() == 3):
         if (self.score_player_one >  self.score_player_two):
            self.visual.player_one_winner()
      else:
         self.player_one.clean_hand()
         self.player_two.clean_hand()
         self.draw()
         print("deck", self.cards.get_deck())
         print("h1", self.player_one.get_hand())
         print("h2", self.player_two.get_hand())
         self.visual.config_image(self.player_one.get_hand(), self.player_two.get_hand(), self.especial_card)
         self.visual.show_labels_buttons()
      
   def sum_score(self):
      self.score_player_one = self.score_player_one + 1
   
   def reset_values(self):
      self.player_one.set_value(0)
      self.player_two.set_value(0)

   def verify_number(self):
      print("o", self.player_one.get_value())
      print("t", self.player_two.get_value())
      if (self.player_one.get_value() <= self.player_two.get_value()):
         return True
      else:
         return False

   def verify_suit(self, index):
      # Verifica si son del mismo tipo 
      suit_player_two = self.get_suit(self.player_two.get_hand()[index])
      print("c", self.especial_card)
      print("a", suit_player_two)
      print("b", self.player_one.get_playing_card())
      if suit_player_two in self.player_one.get_playing_card() or suit_player_two in self.especial_card:
         return True
      else:
         return False
      
   def get_suit(self, string):
      self.suit = ""
      suits = ["spades", "clubs", "hearts", "diamonds"]

      for x in suits:
         if x in string:
            self.suit = x
            break
      
      return self.suit

   def get_special_card(self):
      return self.especial_card
   
   def save_game(self):
       with open('game.csv', 'w') as file:
         write = csv.writer(file)
         write.writerow(self.cards.get_deck())
         write.writerow(self.player_one.get_hand())
         write.writerow(self.player_two.get_hand())

         special_card_list = []
         special_card_list.append(self.especial_card)
         write.writerow( special_card_list)


   def select_especial_card(self):
      """
         El parametro cards debe ser un objeto (El objeto es tipo Mazo)

         Esta funcion retorna una carta del mazo
      """

      return self.cards.deal_cards()

   def draw(self):
      """
         Reparte las cartas a los jugadores

         El parametro cards debe ser un objeto (El objeto es tipo mazo)
         El parametro player_one debe ser un objeto (El objeto es tipo player)
         El parametro player_two debe ser un objeto (El objeto es tipo player)

         Esta funcion no retorna nada
      """

      # Caso en que quedan mas de 12 cartas para repartir
      if (self.player_one.get_size_hand() == 0) or (self.player_two.get_size_hand() == 0) and len(self.cards.deck) > 12:
         for index in range(6*2):
               if (index <= 5):
                  card = self.cards.deal_cards()
                  self.player_one.append_card(card)
               else:
                  card = self.cards.deal_cards()
                  self.player_two.append_card(card)
      # Caso en que quedan menos de 12 cartas para repartir
      """elif (self.player_one.get_size_hand() == 0) or (self.player_two.get_size_hand() == 0) and len(self.cards.deck) < 12:
            for index in range(1):
               if (index == 0):
                  card = self.cards.deal_cards()
                  self.player_one.append_card(card)
               else:
                  card = self.cards.deal_cards()
                  self.player_two.append_card(card) # 1 + 12 = 13 + 12 = 25 + 12 + = 37 + 12 = 49"""
      
   def next_turn(self):
      """
         No implementado aun  
      """

      print("Hola")
      
   def set_rules(self):
      """
         No implementado aun  
      """

      print("Hola2")
      
   def get_state(self):
      """
         No implementado aun  
      """
      
      print("Hola3")

   def get_card(self):
      """
         No implementado aun  
      """

      print("Hola4")

   def end(self):
      """
         No implementado aun  
      """

      print("Hola5")



    
 