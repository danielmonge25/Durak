from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from PIL import Image, ImageTk

class Visual:
    def __init__(self, reglas):
        # Juego Principal
        global root
        root = Tk()
        root.title('Durak game')
        root.geometry("1200x800")
        root.configure(background="green")

        frame = Frame(root, bg="green")
        frame.pack(pady=20)

        self.reglas = reglas

        # Seleccion

        self.seleccion_frame = LabelFrame(frame, text="", bd=0, bg='green')
        self.seleccion_frame.pack(padx=10, ipadx=20)

        self.seleccion_label = Label(self.seleccion_frame, text='Seleccione su turno', font=("Arial", 20), bg='green')
        self.seleccion_label.grid(row=0, column=0, pady=20, padx = 20)

        
        # Crea imagen para las cartas de los jugadores
        self.player_one_frame = LabelFrame(frame, text="Jugador 1", bd=0)
        self.player_one_frame.pack(padx=20, ipadx=20)

        self.player_two_frame = LabelFrame(frame, text="Jugador 2", bd=0)
        self.player_two_frame.pack(ipadx=10, pady=10)

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


    def begin_player_one():
        #messagebox.showinfo("Inicia el jugador 1")
        print("A")

    def begin_player_two():
        #messagebox.showinfo("Inicia el jugador 2")
        print("A")

    
 
    def show_game(self):
        while (self.flag) :
            myButton = Button(root, text="Mostrar Reglas", command=self.click)
            myButton.pack()
            root.mainloop()

    def pick_turn(self):
        f = font.Font(size=15)
        self.player_one_frame.pack_forget()
        self.player_two_frame.pack_forget()
        self.myButtonFirst = Button(root, text="Primero", command=self.first_turn, width=25)
        self.myButtonFirst['font'] = f
        self.myButtonSecond = Button(root, text="Segundo", command=self.second_turn, width=25)
        self.myButtonSecond['font'] = f
        self.myButtonFirst.pack(pady = 5)
        self.myButtonSecond.pack(pady = 5)
        self.flag = True

    def click(self):
        messagebox.showinfo("Reglas", self.reglas)

    def first_turn(self):
        messagebox.showinfo("Turno", "Tu turno es de Primero!")
        self.player_one_frame.pack(padx=20, ipadx=20)
        self.player_two_frame.pack(ipadx=10, pady=10) 
        self.myButtonFirst.pack_forget()
        self.myButtonSecond.pack_forget()
        self.seleccion_frame.pack_forget()
         

    def second_turn(self):
        messagebox.showinfo("Turno", "Tu turno es de Segundo!")
        self.player_one_frame.pack(padx=20, ipadx=20)
        self.player_two_frame.pack(ipadx=10, pady=10)  
        self.myButtonFirst.pack_forget()
        self.myButtonSecond.pack_forget()
        self.seleccion_frame.pack_forget()

    def clean_old_cards(self):
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

    def resize_cards(self, deck_player, index):
         card_image_player = Image.open(f'../cards/{deck_player[index]}.png')
         card_resize_image_player = card_image_player.resize((150, 218))
         card_image_final_player = ImageTk.PhotoImage(card_resize_image_player)

         return card_image_final_player

    def config_image(self, deck_player_one, deck_player_two):
        global card_image_final_player_one, card_image_final_player_two, card_image_final_player_three, card_image_final_player_four
        global card_image_final_player_five, card_image_final_player_six, card_image_final_player_seven, card_image_final_player_eight
        global card_image_final_player_nine, card_image_final_player_ten, card_image_final_player_eleven, card_image_final_player_twelve

        for index in range(len(deck_player_one)):
            # Jugador 1
            print("1", deck_player_one[index])

            # Jugador 2
            """card_image_player_two = Image.open(f'../cards/{deck_player_two[index]}.png')
            card_resize_image_player_two = card_image_player_two.resize((150, 218))
            card_image_final_player_two = ImageTk.PhotoImage(card_resize_image_player_two)"""
            print("2", deck_player_two[index])

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

    def player_defend():
        messagebox.showinfo("El jugador se defendio")
        #cad_button.config(state="disabled")

    def set_reglas(self,reglas):
        self.reglas = reglas
        
    
 