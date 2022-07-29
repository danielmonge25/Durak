'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

class Card:
    def __init__(self):
        """
            Constructor de la clase Card

            Esta funcion no retorna nada
        """

        # Guarda el numero y tipo de la carta
        self.name = ""
    
    def __str__(self):
        """
            Esta funcion devuelve una string con el nombre de la carta
        """

        return self.name

    def set_card_name(self, name):
        """
            Esta funcion establece el nombre y el tipo de la carta
        """

        self.name = name
