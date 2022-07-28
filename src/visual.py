'''
Creado el 26 de Junio del 2022 

@autores: Fernando Aguero, Daniel Monge, Alejandro Sanchez, Andre Villegas
'''

from ast import Index
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk

class Visual:
    def __init__(self, player_one, player_two):
        """
            Constructor de la clase visual

            El parametro player_one debe ser objeto de la clase player
            El parametro player_two debe ser objeto de la clase player

            Esta funcion no retorna nada
        """
        
        # Interfaz principal del juego
        global root
        root = Tk()
        root.title(f'Durak game') # - {len(deck)} Cartas faltantes
        root.geometry("1200x800")
        root.configure(background="green")

        # Crea frame para la carta especial y carta del adversario
        frame_cards = Frame(root, bg="green")
        frame_cards.pack(pady=20)

        # Crea el frame para las cartas
        frame = Frame(root, bg="green")
        frame.pack(pady=10)

        #self.reglas = reglas
        self.player = 0
        self.count_player_one = 0
        self.count_player_two = 0
        self.config = False
        self.card = 0


        # Crea el frame y labels para la seleccion de jugador
        self.seleccion_frame = LabelFrame(frame, text="", bd=0, bg='green')
        self.seleccion_frame.pack(padx=10, ipadx=20)

        self.seleccion_label = Label(self.seleccion_frame, text='Seleccione su turno', font=("Arial", 20), bg='green')
        self.seleccion_label.grid(row=0, column=0, pady=20, padx = 20)

        # Crea imagen para la carta especial y coloca cartas en la imagen
        self.especial_card_frame = LabelFrame(frame_cards, text = "Carta especial", bd=0)  
        self.especial_card_frame.grid(row=0, column=0, padx=20, ipadx=20) 

        self.especial_card_label = Label(self.especial_card_frame, text='')
        self.especial_card_label.pack(pady=20)

        # Crea imagen para la carta que jugo el adversario
        self.played_card_frame = LabelFrame(frame_cards, text="Carta del adversario", bd = 0)
        self.played_card_frame.grid(row=0, column=1, ipadx=20) 

        self.played_card_label = Label(self.played_card_frame, text='')
        self.played_card_label.pack(pady=20)

        # Crea imagen para las cartas de los jugadores
        self.player_one_frame = LabelFrame(frame, text="Jugador 1", bd=0)
        self.player_one_frame.pack(padx=10, ipadx=10)

        self.player_two_frame = LabelFrame(frame, text="Jugador 2", bd=0)
        self.player_two_frame.pack(ipadx=10, pady=10)
        
        #Creacion de los botones para saber quien va primero
        f = font.Font(size=15)
        self.myButtonFirst = Button(root, text="Primero", command=self.first_turn, width=25)
        self.myButtonFirst['font'] = f
        self.myButtonSecond = Button(root, text="Segundo", command=self.first_turn, width=25) #second_turn
        self.myButtonSecond['font'] = f
        self.myButtonFirst.pack(pady = 5)
        self.myButtonSecond.pack(pady = 5)

        # Coloca las cartas en la imagen
        # Para el jugador 1
        self.player_one_label_1 = Label(self.player_one_frame, text='')
        self.player_one_label_1.grid(row=1, column=0, pady=10, padx = 20)

        self.player_one_label_2 = Label(self.player_one_frame, text='')
        self.player_one_label_2.grid(row=1, column=1, pady=10, padx = 20)

        self.player_one_label_3 = Label(self.player_one_frame, text='')
        self.player_one_label_3.grid(row=1, column=2, pady=10, padx = 20)

        self.player_one_label_4 = Label(self.player_one_frame, text='')
        self.player_one_label_4.grid(row=1, column=3, pady=10, padx = 20)

        self.player_one_label_5 = Label(self.player_one_frame, text='')
        self.player_one_label_5.grid(row=1, column=4, pady=10, padx = 20)

        self.player_one_label_6 = Label(self.player_one_frame, text='')
        self.player_one_label_6.grid(row=1, column=5, pady=10, padx = 20)

        # Para el jugador 2 
        self.player_two_label_1 = Label(self.player_two_frame, text='')
        self.player_two_label_1.grid(row=1, column=0, pady=10, padx=20)

        self.player_two_label_2 = Label(self.player_two_frame, text='')
        self.player_two_label_2.grid(row=1, column=1, pady=10, padx=20)

        self.player_two_label_3 = Label(self.player_two_frame, text='')
        self.player_two_label_3.grid(row=1, column=2, pady=10, padx=20)

        self.player_two_label_4 = Label(self.player_two_frame, text='')
        self.player_two_label_4.grid(row=1, column=3, pady=10, padx=20)

        self.player_two_label_5 = Label(self.player_two_frame, text='')
        self.player_two_label_5.grid(row=1, column=4, pady=10, padx=20)

        self.player_two_label_6 = Label(self.player_two_frame, text='')
        self.player_two_label_6.grid(row=1, column=5, pady=10, padx=20)

        # Creacion del frame de los botones de las cartas
        self.button_frame = Frame(root, bg="green")
        self.button_frame.pack(pady=5, padx=200)

        self.button_two_frame = Frame(root, bg="green")
        self.button_two_frame.pack(pady=10)

        # Creacion de botones
        # Botones para el jugador 1
        self.card1 = Button(self.button_frame, text="Primera carta", command=lambda: self.buttons_card(player_one, player_two, 0))
        self.card1.grid(row=0, column=2, padx=37)
        
        self.card2 = Button(self.button_frame, text="Segunda carta", command=lambda: self.buttons_card(player_one, player_two, 1))
        self.card2.grid(row=0, column=4, padx=37)

        self.card3 = Button(self.button_frame, text="Tercera carta", command=lambda: self.buttons_card(player_one, player_two, 2))
        self.card3.grid(row=0, column=6, padx=37)

        self.card4 = Button(self.button_frame, text="Cuarta carta", command=lambda: self.buttons_card(player_one, player_two, 3))
        self.card4.grid(row=0, column=8, padx=37)

        self.card5 = Button(self.button_frame, text="Quinta carta", command=lambda: self.buttons_card(player_one, player_two, 4))
        self.card5.grid(row=0, column=10, padx=37)

        self.card6 = Button(self.button_frame, text="Sexta carta", command=lambda: self.buttons_card(player_one, player_two, 5))
        self.card6.grid(row=0, column=12, padx=37)

        # Botones para el jugador 2
        self.card1_two = Button(self.button_two_frame, text="Primera carta", command=lambda: self.buttons_card(player_one, player_two, 0))
        self.card1_two.grid(row=0, column=2, padx=37)
        
        self.card2_two = Button(self.button_two_frame, text="Segunda carta", command=lambda: self.buttons_card(player_one, player_two, 1))
        self.card2_two.grid(row=0, column=4, padx=37)

        self.card3_two = Button(self.button_two_frame, text="Tercera carta", command=lambda: self.buttons_card(player_one, player_two, 2))
        self.card3_two.grid(row=0, column=6, padx=37)

        self.card4_two = Button(self.button_two_frame, text="Cuarta carta", command=lambda: self.buttons_card(player_one, player_two, 3))
        self.card4_two.grid(row=0, column=8, padx=37)

        self.card5_two = Button(self.button_two_frame, text="Quinta carta", command=lambda: self.buttons_card(player_one, player_two, 4))
        self.card5_two.grid(row=0, column=10, padx=37)

        self.card6_two = Button(self.button_two_frame, text="Sexta carta", command=lambda: self.buttons_card(player_one, player_two, 5))
        self.card6_two.grid(row=0, column=12, padx=37)

        # Creacion del frame de los botones de opciones
        self.button_options_frame = Frame(root, bg="green")
        self.button_options_frame.pack(pady=5, padx= 100)

         # Creacion del boton de guardado
        self.save_button = Button(self.button_options_frame, text="Guardar juego", command=self.click_save_button)
        self.save_button.grid(row=3, column=4, padx=15, pady=20)

        # Boton de las reglas
        self.helpButton= Button(self.button_options_frame, text="Mostrar Reglas", command=self.help)
        self.helpButton.grid(row=3, column=12, padx=15, pady=20)

        # Boton para cargar juego
        self.load_button = Button(self.button_options_frame, text="Cargar juego", command=self.click_load_button)
        self.load_button.grid(row=3, column= 1, padx=20, pady=10)

        # Boton para rendirse
        self.surrender_button = Button(self.button_options_frame, text="Rendirse", command=self.surrender)
        self.surrender_button.grid(row=3, column=0, padx=20)

    def help(self):
        """
            Muestra las reglas del juego

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Reglas", self.reglas)
    
    def click_save_button(self):
        """
            LLama al metodo de guardar partida de la clase durak

            Esta funcion no retorna nada
        """

        self.game.save_game()
        root.destroy()

    def click_load_button(self):
        """
            Establece la interfaz de la partida que se cargo

            Esta funcion no retorna nada
        """

        player = self.game.load_game()
        if(player != 0):
          self.set_player(player)
          messagebox.showinfo("Cargar juego", "Cargando juego...")
          self.config_image(self.game.player_one.get_hand(), self.game.player_two.get_hand(), self.game.get_special_card())
          if (player == "1"):
            self.first_turn()
          else:
            self.second_turn()
        else:
          messagebox.showinfo("Error", "No existe archivo de partida guardada")

    def surrender(self):
        """
            Establece la interfaz para la siguiente ronda

            Esta funcion no retorna nada
        """

        self.game.next_round()
        
        # Quita y agrega botones
        self.player_two_frame.pack_forget()
        self.button_two_frame.pack_forget()
        self.surrender_button.grid_forget()

        self.button_options_frame.pack_forget()

        self.button_frame.pack(pady=10)
        self.player_one_frame.pack(ipadx=10, pady=10)

        self.button_options_frame.pack(pady=5, padx=100)

        self.player = 1
        self.count_player_two = 0
        self.count_player_one = 0
    
    def buttons_card(self, player_one, player_two, index):
        """
            Establece la interfaz de despues de la jugada de uno de los dos jugadores

            El parametro player_one debe ser objeto de la clase player
            El parametro player_one debe ser objeto de la clase player
            El parametro index debe ser int (Posicion del arreglo donde se encuentra la carta a jugar)
            Esta funcion no retorna nada
        """

        if self.player == 1: # Atacante
            #print("Antes 1", player_one.get_hand())

            player_one.set_value_hand(index)
            # Saca la carta de la mano
            player_one.remove_card(index)

            self.config_image_played_card(player_one.get_playing_card())
            # Quita y agrega botones
            self.player_one_frame.pack_forget()
            self.button_frame.pack_forget()

            self.button_options_frame.pack_forget()

            self.button_two_frame.pack(pady=10)
            self.player_two_frame.pack(ipadx=10, pady=10) 

            self.button_options_frame.pack(pady=5, padx=100)
            self.surrender_button.grid(row=3, column=2, padx=20)
           
            
            #print("Despues 1", player_one.get_hand())

            self.player = 2

            self.config_image(player_one.get_hand(), player_two.get_hand(), self.game.get_special_card()) # 5 6 7 0 9 9

            if (self.count_player_one == 0):  
                self.player_one_label_6.grid_forget()  
                self.card6.grid_forget()
                self.count_player_one = self.count_player_one + 1

            elif (self.count_player_one == 1):
                self.player_one_label_5.grid_forget()
                self.card5.grid_forget()
                self.count_player_one = self.count_player_one + 1

            elif (self.count_player_one == 2):
                self.player_one_label_4.grid_forget()
                self.card4.grid_forget()
                self.count_player_one = self.count_player_one + 1

            elif (self.count_player_one == 3):
                self.player_one_label_3.grid_forget()
                self.card3.grid_forget()
                self.count_player_one = self.count_player_one + 1

            elif (self.count_player_one == 4):
                self.player_one_label_2.grid_forget()
                self.card2.grid_forget()
                self.count_player_one = self.count_player_one + 1

            elif (self.count_player_one == 5):
                self.player_one_label_1.grid_forget()
                self.card1.grid_forget()
                self.count_player_one = self.count_player_one + 1
        else: # Defensor
            
            if (self.game.verify_suit(index) == True): 
                player_two.set_value_hand(index)
                if(self.game.verify_number() == True):
                    #print("Antes 2", player_two.get_hand())

                    player_two.remove_card(index)

                    self.config_image_played_card(player_two.get_playing_card())


                    self.player_two_frame.pack_forget()
                    self.button_two_frame.pack_forget()
                    self.surrender_button.grid_forget()

                    self.button_options_frame.pack_forget()
                    
                    self.player_one_frame.pack(ipadx=10, pady=10)
                    self.button_frame.pack(pady=10)

                    self.button_options_frame.pack(pady=5, padx=100)

                    #print("Despues 2", player_two.get_hand())

                    self.player = 1

                    self.config_image(player_one.get_hand(), player_two.get_hand(), self.game.get_special_card())

                    if (self.count_player_two == 0):  
                        self.player_two_label_6.grid_forget()  
                        self.card6_two.grid_forget()
                        self.count_player_two = self.count_player_two + 1

                    elif (self.count_player_two == 1):
                        self.player_two_label_5.grid_forget()
                        self.card5_two.grid_forget()
                        self.count_player_two = self.count_player_two + 1

                    elif (self.count_player_two == 2):
                        self.player_two_label_4.grid_forget()
                        self.card4_two.grid_forget()
                        self.count_player_two = self.count_player_two + 1

                    elif (self.count_player_two == 3):
                        self.player_two_label_3.grid_forget()
                        self.card3_two.grid_forget()
                        self.count_player_two = self.count_player_two + 1

                    elif (self.count_player_two == 4):
                        self.player_two_label_2.grid_forget()
                        self.card2_two.grid_forget()
                        self.count_player_two = self.count_player_two + 1

                    elif (self.count_player_two == 5):
                        self.player_two_label_1.grid_forget()
                        self.card1_two.grid_forget()
                        self.count_player_two = self.count_player_two + 1

                    self.show_winner()
                    self.game.reset_values()
                else:
                    messagebox.showinfo("Restriccion", "Se debe jugar una carta mayor")
            else: 
                messagebox.showinfo("Restriccion", "Se debe jugar el mismo palo")

    def player_one_winner(self):
        """
            Muestra un mensaje diciendo que gano el jugador atacante

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Victoria", "El jugador 1 gano la partida")
        root.destroy()

    def player_two_winner(self):
        """
            Muestra un mensaje diciendo que gano el jugador defensor

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Victoria", "El jugador 1 gano la partida")
        root.destroy()
    
    def show_game(self):
        """
            Muestra la interfaz principal del juego

            Esta funcion no retorna nada
        """

        root.mainloop()

    def show_winner(self):
        """
            Muestra quien gano la partida

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Ganador", "El jugador 2 gano esta ronda")

    def show_buttons_cards(self):
        """
            Muestra la interfaz de los botones de opciones

            Esta funcion no retorna nada
        """

        self.button_frame.pack(pady=10)

    def show_save_button(self):
        """
            Muestra la interfaz del boton de guardado

            Esta funcion no retorna nada
        """

        self.button_options_frame.pack(pady=5, padx=100)
        self.save_button.grid(row=4, column=4, padx=15, pady=20)
    
    def show_labels_buttons(self):
        """
            Establece los labels de las cartas y los botones

            Esta funcion no retorna nada
        """

        # Para el jugador 1
        self.player_one_label_1.grid(row=0, column=0, pady=10, padx = 20)
        self.player_one_label_2.grid(row=0, column=1, pady=10, padx = 20)
        self.player_one_label_3.grid(row=0, column=2, pady=10, padx = 20)
        self.player_one_label_4.grid(row=0, column=3, pady=10, padx = 20)
        self.player_one_label_5.grid(row=0, column=4, pady=10, padx = 20)
        self.player_one_label_6.grid(row=0, column=5, pady=10, padx = 20)

        # Para el jugador 2 
        self.player_two_label_1.grid(row=1, column=0, pady=10, padx=20)
        self.player_two_label_2.grid(row=1, column=1, pady=10, padx=20)
        self.player_two_label_3.grid(row=1, column=2, pady=10, padx=20)
        self.player_two_label_4.grid(row=1, column=3, pady=10, padx=20)
        self.player_two_label_5.grid(row=1, column=4, pady=10, padx=20)
        self.player_two_label_6.grid(row=1, column=5, pady=10, padx=20)

        # Botones para el jugador 1
        self.card1.grid(row=0, column=2, padx=37)
        self.card2.grid(row=0, column=4, padx=37)
        self.card3.grid(row=0, column=6, padx=37)
        self.card4.grid(row=0, column=8, padx=37)
        self.card5.grid(row=0, column=10, padx=37)
        self.card6.grid(row=0, column=12, padx=37)

        # Botones para el jugador 2
        self.card1_two.grid(row=0, column=2, padx=37)
        self.card2_two.grid(row=0, column=4, padx=37)
        self.card3_two.grid(row=0, column=6, padx=37)
        self.card4_two.grid(row=0, column=8, padx=37)
        self.card5_two.grid(row=0, column=10, padx=37)
        self.card6_two.grid(row=0, column=12, padx=37)

    def hide_board(self):
        """
            Oculta todo lo que no sea relacionado a las opciones para elegir quien va primero

            Esta funcion retorna el jugador que va primero
        """

        self.player_one_frame.pack_forget()
        self.player_two_frame.pack_forget()
        
        self.especial_card_frame.grid_forget()
        self.played_card_frame.grid_forget()

        self.button_frame.pack_forget()
        self.button_two_frame.pack_forget()

        self.save_button.grid_forget()
        self.surrender_button.grid_forget()
    
    def first_turn(self):
        """
            Muestra la mano del primer jugador

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Turno", "Tu turno es de Primero!")
        self.player_one_frame.pack(padx=10, ipadx=10)

        self.especial_card_frame.grid(row=1, column=0, padx=20, ipadx=20) 

        self.played_card_frame.grid(row=1, column=1, ipadx=20)

        self.myButtonFirst.pack_forget()
        self.myButtonSecond.pack_forget()
        self.seleccion_frame.pack_forget()
        
        self.load_button.grid_forget()
        self.button_options_frame.pack_forget()

        # Muestra los botones de las cartas
        self.show_buttons_cards()
        # Muestra el boton de guardar partida
        self.show_save_button()

        self.player = 1
        
    def second_turn(self):
        """
            Muestra la mano del primer jugador

            Esta funcion no retorna nada
        """

        messagebox.showinfo("Turno", "Tu turno es de Segundo!")
        self.player_two_frame.pack(ipadx=10, pady=10)  

        self.especial_card_frame.grid(row=1, column=0, padx=20, ipadx=20) 

        self.myButtonFirst.pack_forget()
        self.myButtonSecond.pack_forget()
        self.seleccion_frame.pack_forget()

        self.load_button.grid_forget()
        self.button_options_frame.pack_forget()
        
        # Muestra los botones de las cartas
        self.show_buttons_cards()

        # Muestra el boton de guardar partida
        self.show_save_button()

        self.player = 2

    def resize_cards(self, deck_player, index):
        """
            Establece la imagen de la carta

            El parametro reglas debe ser un string (Carta del jugador)
            El parametro index debe ser un entero (Posicion de la carta en el arreglo)

            Esta funcion retorna la imagen de la carta
        """
    
        card_image_player = Image.open(f'../cards/{deck_player[index].get_card_name()}.png')
        card_resize_image_player = card_image_player.resize((150, 218))
        card_image_final_player = ImageTk.PhotoImage(card_resize_image_player)

        return card_image_final_player

    def config_image_played_card(self, card):
        """
            Configura las imagenes de la carta que jugo el adversario

            El parametro card debe ser un string (Carta del adversario)

            El uso de variables globales es porque sino tkinter no funciona

            Esta funcion no retorna nada
        """

        global played_card_image_final

        played_card_image = Image.open(f'../cards/{card.get_card_name()}.png')
        played_card_resize_image = played_card_image.resize((150, 218))
        played_card_image_final = ImageTk.PhotoImage(played_card_resize_image)
        self.played_card_label.config(image=played_card_image_final)

    def config_image(self, deck_player_one, deck_player_two, card):
        """
            Configura las imagenes de las cartas a la interfaz

            El parametro deck_player_one debe ser un arreglo de strings (Mano del jugador 1)
            El parametro deck_player_two debe ser un arreglo de strings (Mano del jugador 2)
            El parametro card debe ser un string (Carta especial)

            El uso de variables globales es porque sino tkinter no funciona

            Esta funcion no retorna nada
        """

        global card_image_final_player_one, card_image_final_player_two, card_image_final_player_three, card_image_final_player_four
        global card_image_final_player_five, card_image_final_player_six, card_image_final_player_seven, card_image_final_player_eight
        global card_image_final_player_nine, card_image_final_player_ten, card_image_final_player_eleven, card_image_final_player_twelve
        global card_image_final_especial_card
    
        card_image_player = Image.open(f'../cards/{card.get_card_name()}.png')
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

    def get_player(self):
        """
            Esta funcion devuelve el el objeto de la clase player
        """

        return self.player

    def set_player(self, player):
        """
            Establece el objeto de la clase player

            El parametro player debe ser objeto de la clase player

            Esta funcion no retorna nada
        """

        self.player = player
    
    def set_reglas(self, reglas):
        """
            Establece las reglas del juego

            El parametro reglas debe ser string

            Esta funcion no retorna nada
        """

        self.reglas = reglas

    def set_game(self, durak_game):
        """
            Establece el objeto de la clase durak

            El parametro durak_game debe ser objeto de la clase durak

            Esta funcion no retorna nada
        """
        
        self.game = durak_game 