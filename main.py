import tkinter
from PIL import Image, ImageTk
import random
import threading



dice = ['red1.jpeg', 'red2.jpeg', 'red3.jpeg', 'red4.jpeg', 'red5.jpeg', 'red6.jpeg']
# create main window of the application
root = tkinter.Tk()
root.geometry('1280x720')
root.title('JEU DE DE')
root.configure(bg='black')

i1 = tkinter.PhotoImage(file='red6.png')
root.iconphoto(False, i1)





# initialize images


image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

image3 = ImageTk.PhotoImage(Image.open(dice[5]))
label3 = tkinter.Label(root, image=image3, border=10)
label1 = tkinter.Label(root, image=image1, border=0)
label2 = tkinter.Label(root, image=image2, border=0)
label1.configure(image=image1)
label2.configure(image=image2)
label1.pack(side=tkinter.LEFT, padx=30)
label2.pack(side=tkinter.RIGHT, padx=30)

label_result = tkinter.Label(root, text="Resultat: ", width=45, height=10)
label_result.place(x=430, y=250)



class joueur:
    def __init__(self, name="", lvl="", p=True):
        self.name = name
        self.lvl = lvl
        self.p = p

    def presentation(self):
        self.name = input("Entrer votre nom: ")
        print(f"Bienvenue sur le jeu de Dé {self.name}")





    def roll_dice(self):


        dice_number1 = random.choice(dice)
        image1 = ImageTk.PhotoImage(Image.open(dice_number1))


        label1.configure(image=image1)
        label1.image = image1

        dice_number2 = random.choice(dice)
        image2 = ImageTk.PhotoImage(Image.open(dice_number2))


        label2.configure(image=image2)
        label2.image = image2

        if dice_number1 == dice_number2:
            if self.name == j1.name:
                print(f"victoire de {j1.name}")
                label_result.configure(text= "Victoire pour joueur N°1")
            elif self.name == j2.name:
                print(f"victoire de {j2.name}")
                label_result.configure(text="Victoire pour joueur N°2")

            else:
                print("RAS")

        elif int(dice_number1[3:4]) > int(dice_number2[3:4]):
            if self.name == j1.name:
                print("aucune victoire pour le joueur 1")
                label_result.configure(text="aucune victoire pour le joueur 1")
            elif self.name == j2.name:
                print("aucune victoire pour le joueur 2")
                label_result.configure(text="aucune victoire pour le joueur 2")
            else:
                print("erreur")

        elif int(dice_number1[3:4]) < int(dice_number2[3:4]):
            if self.name == j1.name:
                print("aucune victoire pour le joueur 1")
                label_result.configure(text="aucune victoire pour le joueur 1")
            elif self.name == j2.name:
                print("aucune victoire pour le joueur 2")
                label_result.configure(text="aucune victoire pour le joueur 2")
            else:
                print("erreur")

        else:
            print("erreur")







    def stop(self):
        root.quit()



j1 = joueur(name="pnj 1", lvl="0")
j2 = joueur(name="pnj2", lvl="0")

print("Joueur N°1:\n")
j1.presentation()
print("Joueur N°2:\n")
j2.presentation()
print("\n\n")

print(f"Affrontement: {(j1.name.upper())} VS {j2.name.upper()}\n\n")

print("----------INSTRUCTION--------")
print(f"vous devez jouer a tour de role\n le joueur {j1.name.upper()} doit lancer les Dés\n puis passer la main au joeur {j2.name.upper()}\n")
print("celui qui aura les faces identiques de Dés remporte la partie")




t1 = threading.Thread(target=j1.roll_dice())
t2 = threading.Thread(target=j2.roll_dice())

t1.start()
t2.start()





button1 = tkinter.Button(root, text='joueur1', bg='blue', command=j1.roll_dice, width=15, borderwidth=5, height=5)
button2 = tkinter.Button(root, text='joueur2', bg='red', command=j2.roll_dice, width=15, borderwidth=5, height=5)
button3 = tkinter.Button(root, text='quitter', bg='yellow', command=j1.stop, width=15, borderwidth=10, height=5)



button1.place(x=750, y=10)
button2.place(x=400, y=10)
button3.place(x=550, y=600)



root.mainloop()

