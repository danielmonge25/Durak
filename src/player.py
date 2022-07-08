'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel MOnge, Alejandro Sanchez, Andre Villegas
'''

class player:
    def __init__(self):
        """
            Constructor de la clase player

            Esta funcion no retorna nada
        """

        self.hand = []

        self.value = 0

        self.name = ""

        self.playing_card = ""    

    def remove_card(self, index):

        self.playing_card = self.hand[index]

        self.value = int(self.hand[index].split("_", 1)[0])

        self.hand.remove(self.hand[index])

    
    def append_card(self, card):
        """
            Guarda una carta a la mano del jugador

            El parametro card debe ser string (Una carta)

            Esta funcion no retorna nada
        """

        self.hand.append(card)
    
    def get_playing_card(self):
        return self.playing_card
        
    def get_size_hand(self):
        """
            Esta funcion devuelve el tamanyo de la mano del jugador
        """

        return len(self.hand)
    
    def get_hand(self):
        """
            Esta funcion devuelve la mano del jugador
        """

        return self.hand

    def get_value(self):
        return self.value

    def get_player_name(self):
        return self.name

    def set_value(self, value):
        self.value = value
    
    def set_player_name(self, name):
        self.name = name

