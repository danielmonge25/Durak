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

    def append_card(self, card):
        """
            Guarda una carta a la mano del jugador

            El parametro card debe ser string (Una carta)

            Esta funcion no retorna nada
        """

        self.hand.append(card)
    
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