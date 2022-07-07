'''
Creado el 26 de Junio del 2022

@autores: Fernando Aguero, Daniel MOnge, Alejandro Sanchez, Andre Villegas
'''

from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk

class Visual:
    def __init__(self, player_one, player_two):
        """
            Constructor de la clase visual

            El parametro reglas debe ser string
            El parametro deck debe ser un arreglo de strings (Mazo del juego)

            Esta funcion no retorna nada
        """
        
        global root
        root = Tk()
        root.title(f'Durak game') # - {len(deck)} Cartas faltantes
        root.geometry("1200x800")
        root.configure(background="green")

        frame = Frame(root, bg="green")
        frame.pack(pady=20)

        #self.reglas = reglas

        self.player = 0

        self.count_player_one = 0
        self.count_player_two = 0
        # Seleccion

        self.seleccion_frame = LabelFrame(frame, text="", bd=0, bg='green')
        self.seleccion_frame.pack(padx=10, ipadx=20)

        self.seleccion_label = Label(self.seleccion_frame, text='Seleccione su turno', font=("Arial", 20), bg='green')
        self.seleccion_label.grid(row=0, column=0, pady=20, padx = 20)

        
        # Crea imagen para las cartas de los jugadores
        self.player_one_frame = LabelFrame(frame, text="Jugador 1", bd=0)
        self.player_one_frame.pack(padx=10, ipadx=10)

        self.player_two_frame = LabelFrame(frame, text="Jugador 2", bd=0)
        self.player_two_frame.pack(ipadx=10, pady=10)

        # Crea imagen para la carta especial y coloca cartas en la imagen
        self.especial_card_frame = LabelFrame(frame, text = "Carta especial", bd=0)  
        self.especial_card_frame.pack(ipadx=10, pady=10)

        self.especial_card_label = Label(self.especial_card_frame, text='')
        self.especial_card_label.grid(row=2, column=5, pady=20, padx = 20) 
        
        # Coloca las cartas en la imagen

        # Para el jugador 1
        self.player_one_label_1 = Label(self.player_one_frame, text='')
        self.player_one_label_1.grid(row=0, column=0, pady=20, padx = 20)

        self.player_one_label_2 = Label(self.player_one_frame, text='')
        self.player_one_label_2.grid(row=0, column=1, pady=20, padx = 20)

        self.player_one_label_3 = Label(self.player_one_frame, text='')
        self.player_one_label_3.grid(row=0, column=2, pady=20, padx = 20)

        self.player_one_label_4 = Label(self.player_one_frame, text='')
        self.player_one_label_4.grid(row=0, column=3, pady=20, padx = 20)

        self.player_one_label_5 = Label(self.player_one_frame, text='')
        self.player_one_label_5.grid(row=0, column=4, pady=20, padx = 20)

        self.player_one_label_6 = Label(self.player_one_frame, text='')
        self.player_one_label_6.grid(row=0, column=5, pady=20, padx = 20)

        # Para el jugador 2 
        self.player_two_label_1 = Label(self.player_two_frame, text='')
        self.player_two_label_1.grid(row=1, column=0, pady=20, padx=20)

        self.player_two_label_2 = Label(self.player_two_frame, text='')
        self.player_two_label_2.grid(row=1, column=1, pady=20, padx=20)

        self.player_two_label_3 = Label(self.player_two_frame, text='')
        self.player_two_label_3.grid(row=1, column=2, pady=20, padx=20)

        self.player_two_label_4 = Label(self.player_two_frame, text='')
        self.player_two_label_4.grid(row=1, column=3, pady=20, padx=20)

        self.player_two_label_5 = Label(self.player_two_frame, text='')
        self.player_two_label_5.grid(row=1, column=4, pady=20, padx=20)

        self.player_two_label_6 = Label(self.player_two_frame, text='')
        self.player_two_label_6.grid(row=1, column=5, pady=20, padx=20)

         # Creacion del frame de los botones de las cartas
        self.button_frame = Frame(root, bg="green")
        self.button_frame.pack(pady=20)

        # Creacion de botones

        # Botones para el jugador 1
        self.card1 = Button(self.button_frame, text="Primera carta", command=lambda: self.first_card(player_one, player_two))
        self.card1.grid(row=0, column=0)
        
        self.card2 = Button(self.button_frame, text="Segunda carta")
        self.card2.grid(row=0, column=1, padx=20)

        self.card3 = Button(self.button_frame, text="Tercera carta")
        self.card3.grid(row=0, column=2, padx=20)

        self.card4 = Button(self.button_frame, text="Cuarta carta")
        self.card4.grid(row=0, column=3, padx=20)

        self.card5 = Button(self.button_frame, text="Quinta carta")
        self.card5.grid(row=0, column=4, padx=20)

        self.card6 = Button(self.button_frame, text="Sexta carta")
        self.card6.grid(row=0, column=5, padx=20)

        # Botones para el jugador 2
        self.card1_two = Button(self.button_frame, text="Primera carta", command=lambda: self.first_card(player_one, player_two))
        self.card1_two.grid(row=0, column=0)
        
        self.card2_two = Button(self.button_frame, text="Segunda carta")
        self.card2_two.grid(row=0, column=1, padx=20)

        self.card3_two = Button(self.button_frame, text="Tercera carta")
        self.card3_two.grid(row=0, column=2, padx=20)

        self.card4_two = Button(self.button_frame, text="Cuarta carta")
        self.card4_two.grid(row=0, column=3, padx=20)

        self.card5_two = Button(self.button_frame, text="Quinta carta")
        self.card5_two.grid(row=0, column=4, padx=20)

        self.card6_two = Button(self.button_frame, text="Sexta carta")
        self.card6_two.grid(row=0, column=5, padx=20)

        self.card = 0
    
    def set_game(self, durak_game):
        self.game = durak_game 

    def first_card(self, player_one, player_two):
        if self.player == 1:
            print("Antes 1", player_one.get_hand())
            player_one.remove_card(0)

            self.player_one_frame.pack_forget()

            self.player_two_frame.pack(ipadx=10, pady=10) 

            print("Despues 1", player_one.get_hand())

            self.player = 2
            self.count_player_one =  self.count_player_one + 1

            if (self.count_player_one == 1):
                self.player_one_label_1.grid_forget()
                self.card6.grid_forget()
            elif (self.count_player_one == 2):
                self.player_one_label_2.grid_forget()
                self.card5.grid_forget()
            elif (self.count_player_one == 3):
                self.player_one_label_3.grid_forget()
                self.card4.grid_forget()
            elif (self.count_player_one == 4):
                self.player_one_label_4.grid_forget()
                self.card3.grid_forget()
            elif (self.count_player_one == 5):
                self.player_one_label_5.grid_forget()
                self.card2.grid_forget()

        else:
            print("Antes 2", player_two.get_hand())
            player_two.remove_card(0)
        
            self.player_two_frame.pack_forget()

            self.player_one_frame.pack(ipadx=10, pady=10)

            print("Despues 2", player_two.get_hand())

            self.player = 1
            self.count_player_two =  self.count_player_two + 1

            if (self.count_player_two == 1):
                self.player_two_label_1.grid_forget()
                self.card6_two.grid_forget()
            elif (self.count_player_two == 2):
                self.player_two_label_2.grid_forget()
                self.card5_two.grid_forget()
            elif (self.count_player_two == 3):
                self.player_two_label_3.grid_forget()
                self.card4_two.grid_forget()
            elif (self.count_player_two == 4):
                self.player_two_label_4.grid_forget()
                self.card3_two.grid_forget()
            elif (self.count_player_two == 5):
                self.player_two_label_5.grid_forget()
                self.card2_two.grid_forget()
    
        self.game.verify_turn()
    
    def show_winner(self, player_name):
        messagebox.showinfo("Ganador", "El jugador 2 gano esta ronda")

    def show_game(self):
        """
            Muestra la interfaz principal del juego

            Esta funcion no retorna nada
        """

        myButton = Button(root, text="Mostrar Reglas", command=self.click)
        myButton.pack()

        root.mainloop()

    def pick_turn(self):
        """
            Muestra las opciones para elegir quien va primero

            Esta funcion no retorna nada
        """
        f = font.Font(size=15)
        self.player_one_frame.pack_forget()
        self.player_two_frame.pack_forget()
        self.especial_card_frame.pack_forget()
        self.button_frame.pack_forget()

        self.myButtonFirst = Button(root, text="Primero", command=self.first_turn, width=25)
        self.myButtonFirst['font'] = f
        self.myButtonSecond = Button(root, text="Segundo", command=self.second_turn, width=25)
        self.myButtonSecond['font'] = f
        self.myButtonFirst.pack(pady = 5)
        self.myButtonSecond.pack(pady = 5)

        return self.player

    def click(self):
        """
            Muestra las reglas del juego

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Reglas", self.reglas)

    def show_buttons_cards(self):
        self.button_frame.pack(pady=20)

    def first_turn(self):
        """
            Muestra la mano del primer jugador

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Turno", "Tu turno es de Primero!")
        self.player_one_frame.pack(padx=10, ipadx=10)
        self.especial_card_frame.pack(ipadx=10, pady=10)
        self.myButtonFirst.pack_forget()
        self.myButtonSecond.pack_forget()
        self.seleccion_frame.pack_forget()

        # Muestra los botones de las cartas
        self.show_buttons_cards()

        self.player = 1
        
         

    def second_turn(self):
        """
            Muestra la mano del primer jugador

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Turno", "Tu turno es de Segundo!")
        self.player_two_frame.pack(ipadx=10, pady=10)  
        self.especial_card_frame.pack(ipadx=10, pady=10)
        self.myButtonFirst.pack_forget()
        self.myButtonSecond.pack_forget()
        self.seleccion_frame.pack_forget()

        # Muestra los botones de las cartas
        self.show_buttons_cards()

        self.player = 2

    def resize_cards(self, deck_player, index):
        """
            Establece la imagen de la carta

            El parametro reglas debe ser un string (Carta del jugador)
            El parametro index debe ser un entero (Posicion de la carta en el arreglo)

            Esta funcion retorna la imagen de la carta
        """
    
        card_image_player = Image.open(f'../cards/{deck_player[index]}.png')
        card_resize_image_player = card_image_player.resize((150, 218))
        card_image_final_player = ImageTk.PhotoImage(card_resize_image_player)

        return card_image_final_player

    def config_image(self, deck_player_one, deck_player_two, card):
        """
            Configura las imagenes de las cartas a la interfaz

            El parametro deck_player_one debe ser un arreglo de strings (Mano del jugador 1)
            El parametro deck_player_two debe ser un arreglo de strings (Mano del jugador 2)
            El parametro card debe ser un string (Carta especial)

            Esta funcion no retorna nada
        """

        global card_image_final_player_one, card_image_final_player_two, card_image_final_player_three, card_image_final_player_four
        global card_image_final_player_five, card_image_final_player_six, card_image_final_player_seven, card_image_final_player_eight
        global card_image_final_player_nine, card_image_final_player_ten, card_image_final_player_eleven, card_image_final_player_twelve
        global card_image_final_especial_card

        card_image_player = Image.open(f'../cards/{card}.png')
        card_resize_image_player = card_image_player.resize((150, 218))
        card_image_final_especial_card = ImageTk.PhotoImage(card_resize_image_player)
        self.especial_card_label.config(image=card_image_final_especial_card)

        for index in range(len(deck_player_one)):
            # Salida de la carta a la pantalla en forma de imagen
            if (index == 0):
                card_image_final_player_one = self.resize_cards(deck_player_one, index)
                self.player_one_label_1.config(image=card_image_final_player_one)
                
                card_image_final_player_two = self.resize_cards(deck_player_two, index)
                self.player_two_label_1.config(image=card_image_final_player_two)
            elif (index == 1):
                card_image_final_player_three = self.resize_cards(deck_player_one, index)
                self.player_one_label_2.config(image=card_image_final_player_three)

                card_image_final_player_four = self.resize_cards(deck_player_two, index)
                self.player_two_label_2.config(image=card_image_final_player_four)
            elif (index == 2):
                card_image_final_player_five = self.resize_cards(deck_player_one, index)
                self.player_one_label_3.config(image=card_image_final_player_five)

                card_image_final_player_six = self.resize_cards(deck_player_two, index)
                self.player_two_label_3.config(image=card_image_final_player_six)
            elif (index == 3):
                card_image_final_player_seven = self.resize_cards(deck_player_one, index)
                self.player_one_label_4.config(image=card_image_final_player_seven)

                card_image_final_player_eight = self.resize_cards(deck_player_two, index)
                self.player_two_label_4.config(image=card_image_final_player_eight)
            elif (index == 4):
                card_image_final_player_nine = self.resize_cards(deck_player_one, index)
                self.player_one_label_5.config(image=card_image_final_player_nine)

                card_image_final_player_ten = self.resize_cards(deck_player_two, index)
                self.player_two_label_5.config(image=card_image_final_player_ten)
            elif (index == 5):
                card_image_final_player_eleven = self.resize_cards(deck_player_one, index)
                self.player_one_label_6.config(image=card_image_final_player_eleven)

                card_image_final_player_twelve = self.resize_cards(deck_player_two, index)
                self.player_two_label_6.config(image=card_image_final_player_twelve) 

    def set_reglas(self,reglas):
        """
            Establece las reglas del juego

            El parametro reglas debe ser string

            Esta funcion no retorna nada
        """

        self.reglas = reglas
        #cad_button.config(state="disabled")

    def clean_old_cards(self):
        """ 
            No utilizado aun
            
            Limpia la imagen de las cartas de ambos jugadores

            Esta funcion no retorna nada
        """

         # Para el jugador 1
        self.player_one_label_1.config(image='')

        self.player_one_label_2.config(image='')

        self.player_one_label_3.config(image='')

        self.player_one_label_4.config(image='')

        self.player_one_label_5.config(image='')

        self.player_one_label_6.config(image='')

        # Para el jugador 2 
        self.player_two_label_1.config(image='')

        self.player_two_label_2.config(image='')

        self.player_two_label_3.config(image='')

        self.player_two_label_4.config(image='')

        self.player_two_label_5.config(image='')

        self.player_two_label_6.config(image='') 