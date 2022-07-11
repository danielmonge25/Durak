﻿'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

import csv
import os.path
from game import Game

"""from visual import Visual
from deck import deck
from player import player"""

class durak(Game):
   def __init__(self, cards, player_one, player_two, visual):
      """
            Constructor de la clase durak

            Esta funcion no retorna nada
      """

      # Reglas del juego
      self.reglas = "El objetivo es descartar todas tus cartas antes que tus oponentes en diferentes rondas de ataque y defensa hasta que no hayan cartas en el mazo.\n Se juega con 36 cartas de la baraja inglesa, de menor a mayor valor: 6 7 8 9 10 J Q K A.\n Antes de empezar se coloca una carta boca arriba que indicará el palo de «triunfo». A cada jugador se le reparten 6 cartas. Si algún jugador tiene todas la cartas rojas, negras o 5 cartas del mismo palo, se vuelve a repartir. En cada ronda hay un defensor y un atacante. Empieza atacando el jugador que tiene la carta de triunfo más baja en su mano. El jugador a su izquierda es el defensor.\n El atacante juega una carta boca arriba sobre la mesa. El defensor debe responder con una carta superior del mismo palo o una carta del palo de triunfo para no perder la defensa. Se pueden realizar tantos ataques como cartas tiene el defensor hasta un máximo de 6. Para volver a atacar debe haber sobre la mesa una carta del mismo valor. Si un jugador no puede atacar más, pasará el turno al jugador de su izquierda.\n Final de la ronda \n La ronda finaliza cuando todos los jugadores han tenido oportunidad de atacar o se ha alcanzado el número máximo de ataques. Si el defensor ha tenido éxito, se descartarán todas las cartas de la mesa y será el primero en atacar en la siguiente ronda. Si ha fracasado, deberá robar todas las cartas de la mesa y perderá el turno de atacar en la siguiente ronda. Al acabar la ronda, todos los jugadores deberán robar del mazo hasta tener de nuevo 6 cartas, por orden primero los jugadores atacantes y por último el defensor.\n Final de la partida \n Gana el primer jugador que no tenga cartas y no haya cartas disponibles para robar. El resto de jugadores seguirán jugando para salvarse de ser el «durak»." 

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
         #print("h1", self.player_one.get_hand())
         #print("h2", self.player_two.get_hand())
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

      # Verifica si son del mismo tipo 
      suit_player_two = self.get_suit(self.player_two.get_hand()[index])
      #print("c", self.especial_card)
      #print("a", suit_player_two)
      #print("b", self.player_one.get_playing_card())
      if suit_player_two in self.player_one.get_playing_card() or suit_player_two in self.especial_card:
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
         Guarda los datos de la partida en un archivo .csv

         Esta funcion no retorna nada
      """
      
      with open('game.csv', 'w') as file:
         write = csv.writer(file)
         if (self.visual.get_player() == 1):
            write.writerow('1')
         else:
            write.writerow('2')
         write.writerow(self.cards.get_deck())
         write.writerow(self.player_one.get_hand())
         write.writerow(self.player_two.get_hand())

         special_card_list = []
         special_card_list.append(self.especial_card)
         write.writerow( special_card_list)

   def load_game(self):
      """
         Carga los datos de la partida de un archivo .csv

         Esta funcion no retorna nada
      """

      if (os.path.exists('game.csv')):
         with open('game.csv', 'r') as file:
            counter = 0
            for line in file:
               if(line != "\n"):
                  if(counter == 0):
                     player = line[0]

                  elif(counter == 1):
                     line = line.rstrip()
                     deck = line.split(',')

                  elif(counter == 2):
                     line = line.rstrip()
                     if (player == '1'):
                        player_one_hand = line.split(',')
                     else:
                        player_two_hand = line.split(',')

                  elif(counter == 3):
                     line = line.rstrip()
                     if (player == '1'):
                        player_two_hand = line.split(',')
                     else:
                        player_one_hand = line.split(',')

                  elif(counter == 4):
                     special_card = line.rstrip()

                  counter += 1
                  
            self.set_deck(deck)
            self.player_one.set_hand(player_one_hand)
            self.player_two.set_hand(player_two_hand)
            self.set_special_card(special_card)
            return player
      else:
         return 0
   
   def get_special_card(self):
      """
            Esta funcion devuelve la carta especial del juego
      """

      return self.especial_card
   
   def get_suit(self, string):
      """
            Esta funcion devuelve el tipo de la carta que el jugador va a jugar
      """

      self.suit = ""
      suits = ["spades", "clubs", "hearts", "diamonds"]

      for x in suits:
         if x in string:
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