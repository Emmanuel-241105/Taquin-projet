from tkinter import *

from graphisme import creation , move_possible 

HEIGHT = 480
WIDTH = 480
largeur_case = WIDTH // 4
hauteur_case = HEIGHT // 4
tags=None
e=0
play=0
l=creation()
def affichage():
        global play,l
        if play==0:
                play+=1
                e=0
                for i in range(4):
                        for j in range(4):
                                e+=1
                                if e!=16:
                                        a=canvas.coords("a"+str(l[i][j]))
                                        canvas.move("a"+str(l[i][j]),j*largeur_case - a[0], i*hauteur_case - a[1])
        else:
               return
def move_check(event):
    global tags
    item = canvas.find_closest(event.x, event.y)[0]  # Trouve l'objet le plus proche
    tag = canvas.gettags(item)# Récupère ses tags
    tags=int(tag[0][1:])
    e=move_possible(tags)
    print(f"Tags :{tag[0][1:]}",type(tag[0][1:]))
    print(e)

def show_coords(event):
    label.config(text=f"X: {event.x}, Y: {event.y}")
fenetre = Tk() # Création de la fenêtre racine
canvas = Canvas(fenetre, bg="white", height=HEIGHT, width=WIDTH)
canvas.pack(side="top")
for i in range(4):
    for j in range(4):
        e+=1
        canvas.create_rectangle((j*largeur_case, i*hauteur_case),
                ((j+1)*largeur_case, (i+1)*hauteur_case), fill="grey",tags="a"+str(e))
        canvas.create_text(((j*largeur_case)+60, (i*hauteur_case)+60),text=str(e),font=("Arial", 60, "bold"),fill="black",tags="a"+str(e))
canvas.delete("a16")
b1=Button(fenetre,text="play" ,font=("arial",10),command=affichage).pack(side="bottom",pady=20)
b2=Button(fenetre,text="aide" ,font=("arial",10)).pack(side="left")
b3=Button(fenetre,text="quitter" ,command= fenetre.destroy ,font=("arial",10)).pack(side="right")
label = Label(fenetre, text="Déplacez la souris", font=("Arial", 14))
label.pack(pady=20)

fenetre.bind("<Motion>", show_coords)  # Détecter le mouvement de la souris
print(l)
canvas.bind("<Button-1>", move_check)


fenetre.mainloop() # Lancement de la boucle principale
