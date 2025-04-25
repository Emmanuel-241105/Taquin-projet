from tkinter import *
from random import choice
from graphisme import creation , move_possible,cherche
from fichier import sauvegarder , lecture
from tkinter.messagebox import *
import math
import random


HEIGHT = 480
WIDTH = 480
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4
tags=None
e=0
play=0 # 1 pour le jeu en cours et 0 pour le jeu terminé et none pour pas en cours
s=0 # 0 pour le jeu en cours et 1 pour le jeu terminé ou # s booléen pour savoir si le mouvement est possible ou pas
cercles=[]
historique = []
l=creation() #
tab=l
score=0
# variables de temps
time=[0,0,0]
def l_move(board,n): # bord c'est le tableau l et n c'est l'élément dont on veut savoir si le déplacement est possible
    move_possible_result=move_possible(n,l)
    zero_position=cherche(0,board)#position du zéro
    target_position=cherche(n,board)# position de la case dont on veut déterminer si le déplacement est possible
    
    if zero_position!=target_position: # Si on clique sur la case 0, on ne fait rien et retourne le board sans modification.
        
     if move_possible_result[0]==0: # Si le mouvement n'est pas possible, retourne le board sans modification.
        return board, False
    
     # Détermine si le mouvement se fait sur la même ligne ou la même colonne
     # Calcul des déplacements
     row_difference = int(target_position[0] - zero_position[0] ) # Différence de ligne
     column_difference = int(target_position[1] - zero_position[1] ) # Déplacement sur les colonnes

     # Déplacement horizontal (même ligne)
     if move_possible_result[1] == 1:
        # Déplacement vers la droite ou vers la gauche selon la différence de colonne
        step = 1 if column_difference > 0 else -1
        for _ in range(abs(column_difference)):
            board[zero_position[0]][zero_position[1]], board[zero_position[0]][zero_position[1] + step] = \
                board[zero_position[0]][zero_position[1] + step], board[zero_position[0]][zero_position[1]]
            zero_position = cherche(0, board)  # Met à jour la position de l'élément 0 après chaque échange
        return board, True
    
     # Déplacement vertical (même colonne) [move_possible_result[1] == 0]
     else :
        # Déplacement vers le bas ou vers le haut selon la différence de ligne
        step = 1 if row_difference > 0 else -1
        for _ in range(abs(row_difference)):
            board[zero_position[0]][zero_position[1]], board[zero_position[0] + step][zero_position[1]] = \
                board[zero_position[0] + step][zero_position[1]], board[zero_position[0]][zero_position[1]]
            zero_position = cherche(0, board)  # Met à jour la position de l'élément 0 après chaque échange
        return board, True
    elif  zero_position!=target_position:
        return board, False

# fonction compteur de temps
def timer():

    """Fonction qui gère le timer."""
    global time
    print(play)
    if play==1:
        time[0] += 1
        if time[0] == 60:
            time[0] = 0
            time[1] += 1
        if time[1] == 60:
            time[1] = 0
            time[2] += 1
    else: # Si le jeu est terminé, on ne met pas à jour le timer
        time[0]=time[0]
        time[1]=time[1]
        time[2]=time[2]
    time_label.config(text="Time:"f"{time[2]:02}:{time[1]:02}:{time[0]:02}")
    fenetre.after(1000, timer)  # Appelle la fonction toutes les secondes
def charger_game():
    global l,time,score
    dico=lecture("save.csv")
    print(dico)
    if dico!={"liste":[],"time":[],"score":[]}:
        l=dico["liste"]
        print(l,l[2],type(l[2]))
        time=dico["time"]
        score=int(dico["score"][0])
        print(score)
        move()

    else:
        showwarning("alerte","vous n'avez pas de sauvegarde")

def save():
    sauvegarder("save.csv",l,time,score)



def move():
    global play,l,s
    if play==0 or s==1:
        fenetre2.destroy()
        play=1
        update_graphical_board(l)
        s=0

def update_graphical_board(boardin:list[list[int]]):
    """Actualise le tableau graphique avec les valeurs du tableau donné."""
    print(l)
    for i in range(4):
        for j in range(4):
            if boardin[i][j]!=0:
                a=canvas.coords("a"+str(boardin[i][j]))
                canvas.move("a"+str(boardin[i][j]),j*largeur_case - a[0], i*hauteur_case - a[1])


def restart():
    """Redémarre le jeu en réinitialisant le tableau graphique."""
    global score, l,time
    score=0
    time=[0,0,0]
    score_label.config(text="nber of moves: " + str(score)) 
    #timer() # Démarre le timer
    l=creation()
    update_graphical_board(l)

# fonction qui verifie si le mouvement est possible
def move_check(event):
    """Vérifie si le mouvement est possible en fonction de la position du clic."""
    global tags,s,l,play,score 
    print("hello",l)
    item = canvas.find_closest(event.x, event.y)[0]  # Trouve l'objet le plus proche
    print(item)
    tag = canvas.gettags(item)  # Récupère ses tags
    tags = int(tag[0][1:])
    print(tags)
    s = move_possible(tags,l)[0]
    print(s)

    # Sauvegarde l'état actuel avant de faire le move
    historique.append([row[:] for row in l])  # Copie profonde de la grille

    l, bool_move = l_move(l, tags)
    score = score + 1 if bool_move else score
    score_label.config(text="nber of moves: " + str(score))  # Met à jour le label
    if play != 0:
        move()
        affichage_gagner(l)
def undo_move():
    global l, historique, score
    if historique:
        l = historique.pop()  # Récupère le dernier état
        update_graphical_board(l)
        score = max(0, score - 1)
        score_label.config(text="nber of moves: " + str(score))


       

def creer_feu_artifice(canvas, x, y, couleur, rayon, nb_parts):
    """ Crée un feu d'artifice à une position donnée avec des éclats de différentes couleurs. """
    for _ in range(nb_parts):
        angle = random.uniform(0, 2 * math.pi)  # Angle aléatoire
        vitesse = random.uniform(3, 6)  # Vitesse aléatoire
        dx = math.cos(angle) * vitesse
        dy = math.sin(angle) * vitesse

        # Création d'une petite ligne (particule du feu d'artifice)
        canvas.create_line(x, y, x + dx * rayon, y + dy * rayon, fill=couleur, width=2)

def afficher_feu_artifice(canvas, x, y):
    """ Affiche plusieurs feux d'artifice avec des couleurs et des vitesses aléatoires. """
    couleurs = ["red", "orange", "yellow", "green", "blue", "purple", "white"]
    for _ in range(5):  # Nombre de feux d'artifice à afficher
        couleur = random.choice(couleurs)
        rayon = random.randint(10, 15)  # Rayon aléatoire pour l'éclat
        nb_parts = random.randint(10, 20)  # Nombre de particules pour chaque feu d'artifice
        creer_feu_artifice(canvas, x, y, couleur, rayon, nb_parts)

def victoire(fenetre_principale, canvas):
    canvas.config(bg="cyan")
    
    # Ajouter le texte "Félicitations!" à la fenêtre principale
    labelvictoire = Label(canvas, text="Félicitations!", font=("Helvetica", 24, "bold"), fg="yellow",bg="red")
    #canvas.create_text(20,50, text="Félicitations Johan !", font=("Helvetica",24, "bold"), fill="purple")
    label_temps_mis=Label(fenetre_principale, text="Temps mis:"f"{time[2]:02}:{time[1]:02}:{time[0]:02}", font=("Helvetica", 24, "bold"), fg="purple")
    label_déplacements=Label(fenetre_principale, text="Nombre de déplacements:"+str(score), font=("Helvetica", 24, "bold"), fg="purple")
    points=int(100000*((1/(1+score))+(1/(3600*time[2]+60*time[1]+time[0]+1))))
    label_points=Label(fenetre_principale,text="Nombre de points:"+str(points) ,font=("Helvetica", 24, "bold"), fg="purple")
    labelvictoire.place(x=140, y=20)  # Placer le texte en haut au centre
    label_temps_mis.place(x=140, y=100)
    label_déplacements.place(x=140,y=175)
    label_points.place(x=140,y=250)
    #creer_ondes()
    #animer()
    # Afficher des feux d'artifice au centre de la fenêtre
    afficher_feu_artifice(canvas, 200, 200)
    afficher_feu_artifice(canvas, 350, 350)
    afficher_feu_artifice(canvas, 50, 200)
    afficher_feu_artifice(canvas, 350, 350)
    afficher_feu_artifice(canvas, 200, 50)
    afficher_feu_artifice(canvas, 250, 350)
    afficher_feu_artifice(canvas, 50, 375)
    afficher_feu_artifice(canvas, 350, 50)
    afficher_feu_artifice(canvas, 200, 400)
    afficher_feu_artifice(canvas, 380, 200)
    afficher_feu_artifice(canvas, 30, 20)
    # Animation de feux d'artifice en boucle
    def animer_feu():
        canvas.delete("all")  # Efface les éléments précédents
        afficher_feu_artifice(canvas, 200, 200)  # Crée de nouveaux feux d'artifice
        afficher_feu_artifice(canvas, 350, 350)
        afficher_feu_artifice(canvas, 50, 200)
        afficher_feu_artifice(canvas, 420, 420)
        afficher_feu_artifice(canvas, 200, 50)
        afficher_feu_artifice(canvas, 250, 350)
        afficher_feu_artifice(canvas, 50, 375)
        afficher_feu_artifice(canvas, 350, 50)
        afficher_feu_artifice(canvas, 200, 400)
        afficher_feu_artifice(canvas, 380, 200)
        afficher_feu_artifice(canvas, 30, 20)
        fenetre_principale.after(500, animer_feu)  # Répète tous les 500 ms (0.5 seconde)
    
    # Démarrer l'animation des feux d'artifice
    animer_feu()


def affichage_gagner(l):
    L= [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    if l==L:
        # victoire
        play=0
        print(play)
        victoire(fenetre, canvas)  # Appel de la fonction de victoire
       # fenetre.destroy() ne pas fermer la fenetre mais ouvrir la fenetre avec le scenario de victoire
   

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

"""""
def congratulations():
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
    fenetre3.after(50, animer) """

fenetre = Tk() # Création de la fenêtre racine
fenetre.focus()
fenetre2=Toplevel(fenetre,bg="black",highlightbackground="red")
"""fenetre2.geometry("300x200")"""
fenetre2.attributes("-topmost", True)
fenetre.title("TAQUIN")
canvas = Canvas(fenetre, bg="white",height=HEIGHT, width=WIDTH)
canvas2 = Canvas(fenetre2,bg="black", height=400, width=400)
canvas2.create_text(200,100, text="Bienvenue sur Taquin", font=("Helvetica",20, "normal"), fill="white")

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

score_label = Label(fenetre, text="nber of moves:"+str(score), font=("Comic Sans MS", 20), bg="white")
score_label.grid(row=6, column=5, padx=10, pady=10)
time_label= Label(fenetre, text="Time: 00:00:00", font=("Comic Sans MS", 20), bg="white")
time_label.grid(row=6, column=10, padx=10, pady=10)
b1=Button(fenetre2,text="nouvelle partie" ,font=("Comic Sans MS",15),command=move)
b4=Button(fenetre2,text="charger partie" ,font=("Comic Sans MS",15),command=charger_game)
b2=Button(fenetre,text="Help" ,font=("Comic Sans MS",20), command= fenetreaide)
b3=Button(fenetre,text="Save" ,command=lambda:sauvegarder("save.csv",l,time,score) ,font=("Comic Sans MS",20))
"""b_undo = Button(fenetre, text="Undo", font=("Comic Sans MS", 20), command=undo_move)
b_undo.grid(row=6, column=1)"""

canvas.grid(row=0,column=5,rowspan=5)
canvas2.grid(row=0,column=0,columnspan=3)
b3.grid(row=7,column=10)
b5=Button(fenetre,text="restart" ,font=("Comic Sans MS",20),command=restart )
b5.grid(row=6,column=0)
b2.grid(row=7,column=5)
canvas2.create_window(200,200, window=b1)
canvas2.create_window(200,250, window=b4)
canvas.bind("<Button-1>", move_check)
creer_ondes()
animer()
timer() # Démarre le timer
parametre = Button(fenetre, text="Setting",font=("Comic Sans MS", 20),command=setting )
parametre.grid(row=7,column=0)
fenetre.mainloop() # Boucle principale de la fenêtre

