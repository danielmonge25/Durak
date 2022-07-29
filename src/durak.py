'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

import csv
import os.path
from game import Game
from CSV_serializer import JSON_Seializer

class durak(Game):
   def __init__(self, cards, player_one, player_two, visual):
      """
            Constructor de la clase durak

            El parametro cards debe ser objeto de la clase deck
            El parametro player_one debe ser objeto de la clase player
            El parametro player_two debe ser objeto de la clase player
            El parametro visual debe ser objeto de la clase visual

            Esta funcion no retorna nada
      """

      # Reglas del juego
      self.reglas = "El objetivo es descartar todas tus cartas antes que tus oponentes en diferentes rondas de ataque y defensa hasta que no hayan cartas en el mazo.\n Se juega con 52 cartas.\n Antes de empezar se coloca una carta boca arriba que indicará el palo de «triunfo». A cada jugador se le reparten 6 cartas. En cada ronda hay un defensor y un atacante.\n El atacante juega una carta boca arriba sobre la mesa. El defensor debe responder con una carta superior del mismo palo o una carta del palo de triunfo para no perder la defensa. Se pueden realizar tantos ataques como cartas tiene el defensor hasta un máximo de 6.\n  Final de la ronda \n La ronda finaliza cuando se ha alcanzado el número máximo de ataques o el defensor no puede defenderse. Si el defensor ha tenido éxito, gana la partida. Si ha fracasado, se descartan las cartas de ambos y deberán robar del mazo hasta tener de nuevo 6 cartas.\n  Final de la partida \n Gana el defensor si se logra defender 6 veces en una ronda o gana el atacante si el defensor no se logra defender 6 veces y ya no quedan cartas en el mazo para robar" 

      # Carta especial del juego
      self.especial_card = ""

      # Puntaje del jugador atacante
      self.score_player_one = 0
      #Puntaje del jugador defensor
      self.score_player_two = 0

      # Objeto de la clase cards
      self.cards = cards
      # Objeto de la clase player
      self.player_one = player_one
      # Objeto de la clase player
      self.player_two = player_two
      # Objeto de la clase visual
      self.visual = visual

      # Objeto de la clase Json_serializer
      self.Json_serializer = JSON_Seializer()

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
      self.visual.hide_board()

      # Muestra el juego
      self.visual.show_game()
   
   def verify_turn(self):
      """
         Verifica si los jugadores tienen cartas

         Esta funcion no retorna nada
      """

      if (self.player_one.get_len_hand() == 0 and self.player_two.get_len_hand() == 0):
         self.visual.player_two_winner()
      
   def next_round(self):
      """
         Prepara el juego para la siguiente ronda

         Esta funcion no retorna nada
      """

      self.sum_score()
      if (self.cards.get_len_deck() == 3):
         if (self.score_player_one >  self.score_player_two):
            self.visual.player_one_winner()
      else:
         self.player_one.clean_hand()
         self.player_two.clean_hand()
         self.draw()
         #print("deck", self.cards.get_deck())
         self.visual.config_image(self.player_one.get_hand(), self.player_two.get_hand(), self.especial_card)
         self.visual.show_labels_buttons()
      
   def sum_score(self):
      """
         Suma el puntaje del jugador 1

         Esta funcion no retorna nada
      """

      self.score_player_one = self.score_player_one + 1
   
   def reset_values(self):
      """
         Reinicia los numeros de las cartas que ambos jugadores usaron

         Esta funcion no retorna nada
      """

      self.player_one.set_value(0)
      self.player_two.set_value(0)

   def verify_number(self):
      """
         Verifica si la carta que jugo el defensor es mayor a la del atacante

         Esta funcion no retorna nada
      """

      #print("o", self.player_one.get_value())
      #print("t", self.player_two.get_value())
      if (self.player_one.get_value() <= self.player_two.get_value()):
         return True
      else:
         return False

   def verify_suit(self, index):
      """
         Verifica si la carta que jugo el defensor es del mismo tipo que la del atacante o de la carta especial

         Esta funcion no retorna nada
      """

      # Tipo de la carta
      suit_player_two = self.get_suit(self.player_two.get_hand()[index])
      #print("HOLA", self.especial_card.get_card_name())
      
      # Verifica si son del mismo tipo 
      if suit_player_two in self.player_one.get_playing_card().get_card_name() or suit_player_two in self.especial_card.get_card_name():
         return True
      else:
         return False

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

   def select_especial_card(self):
      """
         Esta funcion retorna una carta del mazo
      """

      return self.cards.deal_cards()

   def save_game(self):
      """
         LLama al serializador para guardar la partida

         Esta funcion no retorna nada
      """
      self.Json_serializer.serialize_game(self.visual, self.cards, self.player_one, self.player_two, self.especial_card)
      

   def load_game(self):
      if (os.path.exists('game.csv')):
         with open('game.csv', 'r') as file:
            counter = 0
            for line in file:
               if(line != "\n"):
                  if(counter == 0):
                     player = line[0]

                  elif(counter == 1):
                     line = line.rstrip()
                     self.set_deck(line.split(','))

                  elif(counter == 2):
                     line = line.rstrip()
                     if (player == '1'):
                        self.player_one.set_hand(line.split(','))
                     else:
                        self.player_two.set_hand(line.split(','))

                  elif(counter == 3):
                     line = line.rstrip()
                     #print(line)
                     if (player == '1'):
                        self.player_two.set_hand(line.split(','))
                     else:
                        self.player_one.set_hand(line.split(','))

                  elif(counter == 4):
                     self.set_special_card(line.rstrip())

                  counter += 1
               
            return player
      else:
         return 0

   def get_special_card(self):
      """
            Esta funcion devuelve la carta especial del juego
      """

      return self.especial_card
   
   def get_suit(self, card):
      """   
            El parametro visual debe ser objeto de la clase Card
            Esta funcion devuelve el tipo de la carta que el jugador va a jugar
      """

      self.suit = ""
      suits = ["spades", "clubs", "hearts", "diamonds"]

      for x in suits:
         if x in card.get_card_name():
            self.suit = x
            break
      
      return self.suit

   def set_deck(self, deck):
      """
            Esta funcion establece el deck del juego
      """

      self.deck = deck

   def set_special_card(self, special_card):
      """
            Esta funcion establece la carta especial del juego
      """

      self.especial_card = special_card 

   def get_card_name(self, card):
      """
         Esta funcion obtiene el nombre de una carta
      """
      return card.get_card_name