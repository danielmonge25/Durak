'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

class Card:
    def __init__(self):
        """
            Constructor de la clase card

            Esta funcion no retorna nada
        """

        # Guarda el numero y tipo de la carta
        self.card = ""
    
    def get_card_name(self):
        """
            Esta funcion devuelve la carta
        """

        return self.card

    def set_card_name(self, card):
        """
            Esta funcion establece el nombre y el tipo de la carta
        """

        self.card = card
