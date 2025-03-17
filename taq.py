from tkinter import *
from random import choice
from graphisme import creation , move_possible,l_move

HEIGHT = 480
WIDTH = 480
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4
tags=None
e=0
play=0
s=0
cercles=[]
l=creation()
def move():
        global play,l,s
        if play==0 or s==1:
                fenetre2.destroy()
                play=1
                for i in range(4):
                        for j in range(4):
                                if l[i][j]!=0:
                                        a=canvas.coords("a"+str(l[i][j]))
                                        canvas.move("a"+str(l[i][j]),j*largeur_case - a[0], i*hauteur_case - a[1])
                s=0



def move_check(event):
    global tags,s,l,play
    item = canvas.find_closest(event.x, event.y)[0]  # Trouve l'objet le plus proche
    tag = canvas.gettags(item)# Récupère ses tags
    tags=int(tag[0][1:])
    s=move_possible(tags)[0]
    l=l_move(l,tags)
    if play!=0:
        move()
        affichage_gagner(l)    
def victoire():
    fenetrefin = Tk()
    fenetrefin.title("VICTORY")
    labelvictoire = Label(fenetrefin, text="VICTORY")
    labelvictoire.pack(padx=10, pady=10)


def affichage_gagner(l):
    L= [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    if l==L:
        victoire
        fenetre.destroy()

#fonction qui ouvre la fenetre setting
def setting():
      global parametrefenetre
      parametrefenetre = Toplevel(fenetre) 
      parametrefenetre.title("SETTING")
      boutoncouleur = Button(parametrefenetre, text="Color", font=("Comic Sans MS",20), command=color)
      boutoncouleur.pack(side="bottom", padx=80, pady=80)

#fonction pour les boutons de couleurs
def changement_couleur(couleur):
      canvas.config(bg= couleur)

#fonction pour la fenetre palette de couleur
def color():
      palettecouleur = Toplevel(parametrefenetre) 
      palettecouleur.title("PALETTE DE COULEUR")
      bred = Button(palettecouleur, text="red",font=("Comic Sans MS",20), command=lambda: changement_couleur("red"))
      bred.pack(padx=100, pady=20)
      bblack = Button(palettecouleur, text="black",font=("Comic Sans MS",20),  command=lambda: changement_couleur("black"))
      bblack.pack(padx=60, pady=20)
      bgreen = Button(palettecouleur, text="green",font=("Comic Sans MS",20),  command=lambda :changement_couleur("green"))
      bgreen.pack(padx=60, pady=20)
      bblue = Button(palettecouleur, text="blue",font=("Comic Sans MS",20),  command=lambda :changement_couleur("blue"))
      bblue.pack(padx=60, pady=20)
      byellow = Button(palettecouleur, text="yellow",font=("Comic Sans MS",20),  command=lambda :changement_couleur("yellow"))
      byellow.pack(padx=60, pady=20)
      bwhite = Button(palettecouleur, text="white",font=("Comic Sans MS",20),  command=lambda :changement_couleur("white"))
      bwhite.pack(padx=60, pady=20)


def creer_ondes():
    cercle = canvas2.create_oval(200, 200, 200, 200, outline=choice(["red","yellow","blue","white","grey","orange","green","violet"]), width=2)
    cercles.append((cercle, 0))  
    fenetre2.after(500, creer_ondes)  

def animer():
    nouveaux_cercles = []
    for cercle, taille in cercles:
        taille += 5
        x0, y0 = 200 - taille, 200 - taille
        x1, y1 = 200 + taille, 200 + taille
        canvas2.coords(cercle, x0, y0, x1, y1)
        if taille < 200:
            nouveaux_cercles.append((cercle, taille))
        else:
            canvas2.delete(cercle)
    
    cercles.clear()
    cercles.extend(nouveaux_cercles) 
    fenetre2.after(50, animer)  

fenetre = Tk() # Création de la fenêtre racine
fenetre.focus()
fenetre2=Toplevel(fenetre,bg="black",highlightbackground="red")
"""fenetre2.geometry("300x200")"""
fenetre2.attributes("-topmost", True)
fenetre.title("TAQUIN")
canvas = Canvas(fenetre, bg="white",height=HEIGHT, width=WIDTH)
canvas2 = Canvas(fenetre2,bg="black", height=400, width=400)
canvas2.create_text(200,100, text="Taquin", font=("Helvetica", 40, "normal"), fill="white")

def fenetreaide():  
    help = Toplevel(fenetre)
    help.title("HELP")
    texte = Label(help, text="Le jeu du Taquin est un puzzle consistant à déplacer \n"
                             "des cases numérotées dans une grille pour réorganiser l'ordre des cases de manière\n"
                             "à former une séquence correcte. Le but est de déplacer les pièces jusqu'à ce que \n"
                             "l'ordre des chiffres soit rétabli, généralement de gauche à droite et de haut en bas,\n"
                             "avec une case vide permettant de déplacer les autres pièces.", font=("Comic Sans MS", 15))
    texte.pack(padx=10, pady=10)

for i in range(4):
    for j in range(4):
        e+=1
        canvas.create_rectangle((j*largeur_case, i*hauteur_case),
                ((j+1)*largeur_case, (i+1)*hauteur_case), fill="grey",tags="a"+str(e))
        canvas.create_text(((j*largeur_case)+60, (i*hauteur_case)+60),text=str(e),font=("Comic Sans MS", 60, "bold"),fill="black",tags="a"+str(e))
canvas.delete("a16")

b1=Button(fenetre2,text="nouvelle partie" ,font=("Comic Sans MS",15),command=move)
b4=Button(fenetre2,text="charger partie" ,font=("Comic Sans MS",15))
b2=Button(fenetre,text="Help" ,font=("Comic Sans MS",20), command= fenetreaide)
b3=Button(fenetre,text="Quit" ,command= fenetre.destroy ,font=("Comic Sans MS",20))
canvas.grid(row=0,column=5,rowspan=5)
canvas2.grid(row=0,column=0,columnspan=3)
b2.grid(row=6,column=0)
b3.grid(row=6,column=10)
canvas2.create_window(200,200, window=b1)
canvas2.create_window(200,250, window=b4)
canvas.bind("<Button-1>", move_check)
creer_ondes()
animer()
parametre = Button(fenetre, text="Setting",font=("Comic Sans MS", 20),command=setting )
parametre.grid(row=6,column=5)
fenetre.mainloop() 


