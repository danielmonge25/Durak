'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

class player:
    def __init__(self):
        """
            Constructor de la clase player

            Esta funcion no retorna nada
        """

        # Mano del jugador
        self.hand = []

        # numero de la carta que jugo
        self.value = 0

        # Nombre del jugador
        self.name = ""

        # Carta que jugo
        self.playing_card = ""    

    def append_card(self, card):
        """
            Guarda una carta a la mano del jugador

            El parametro card debe ser string (Una carta)

            Esta funcion no retorna nada
        """

        self.hand.append(card)

    def remove_card(self, index):
        """
            Elimina una carta de la mano del jugador

            El parametro index debe ser int (Posicion de la carta en el arreglo)

            Esta funcion no retorna nada
        """

        self.playing_card = self.hand[index]

        self.hand.remove(self.hand[index])

    def clean_hand(self):
        """
            Limpia la mano del jugador 

            Esta funcion no retorna nada
        """

        self.hand = []
    
    def get_playing_card(self):
        """
            Esta funcion devuelve la carta que el jugador va a jugar
        """

        return self.playing_card

    def get_player_name(self):
        """
            Esta funcion devuelve el nombre del jugador
        """

        return self.name
    
    def get_size_hand(self):
        """
            Esta funcion devuelve el tamanyo de la mano del jugador
        """

        return len(self.hand)
    
    def get_len_hand(self):
        """
            Esta funcion devuelve el tamanyo de la mano del jugador
        """

        return len(self.hand)
    
    def get_value(self):
        """
            Esta funcion devuelve el numero de la carta que jugo
        """

        return self.value
    
    def get_hand(self):
        """
            Esta funcion devuelve la mano del jugador
        """

        for index in range(len(self.hand)):
            print(self.hand[index].get_card_name())
        print("\n")

        return self.hand

    def set_hand(self, hand):
        """
            Esta funcion establece la mano del jugador
        """

        self.hand = hand.copy()

    def set_value(self, value):
        """
            Esta funcion establece el valor de la carta que el jugador jugo
        """

        self.value = value
    
    def set_player_name(self, name):
        """
            Esta funcion establece el nombre del jugador
        """

        self.name = name
    
    def set_value_hand(self, index):
        """
            Esta funcion guarda el valor de la carta que el jugador va a jugar
        """

        self.value = int(self.hand[index].get_card_name().split("_", 1)[0])
