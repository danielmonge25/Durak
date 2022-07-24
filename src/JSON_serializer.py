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

         Esta funcion no retorna nada
        """
        with open('game.csv', 'w') as file:
         write = csv.writer(file)
         if (visual.get_player() == 1):
            write.writerow('1')
         else:
            write.writerow('2')
         write.writerow(cards.get_deck())
         write.writerow(player_one.get_hand())
         write.writerow(player_two.get_hand())

         special_card_list = []
         special_card_list.append(special_card)
         write.writerow( special_card_list)
