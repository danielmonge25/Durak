'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

from abstract_serializer import Abstract_Serializer
import csv

class JSON_Seializer(Abstract_Serializer):

    def serialize_game(self, visual, cards, player_one, player_two, special_card):
        """
         Guarda los datos de la partida en un archivo .csv

         El parametro visual debe ser objeto de la clase visual
         El parametro cards debe ser objeto de la clase deck
         El parametro player_one debe ser objeto de la clase player
         El parametro player_two debe ser objeto de la clase player
         El parametro especial_card debe ser objeto de la clase Card
   
         Esta funcion no retorna nada
        """

        with open('game.csv', 'w') as file:
         write = csv.writer(file)
         if (visual.get_player() == 1):
            write.writerow('1')
         else:
            write.writerow('2')
         write.writerow(cards.get_deck()) # Mazo del juego
         write.writerow(player_one.get_hand_save()) # Mano del jugador 1
         write.writerow(player_two.get_hand_save()) # Mano del jugador 2

         special_card_list = []
         special_card_list.append(special_card.get_card_name()) # Carta especial
         write.writerow( special_card_list)
