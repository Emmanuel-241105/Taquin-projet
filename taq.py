from tkinter import *
from random import choice
from graphisme import creation , move_possible,l_move, affichage_gagner

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
                play+=1
                for i in range(4):
                        for j in range(4):
                                if l[i][j]!=0:
                                        a=canvas.coords("a"+str(l[i][j]))
                                        canvas.move("a"+str(l[i][j]),j*largeur_case - a[0], i*hauteur_case - a[1])
                s=0
def color():
      tabcolor=Tk()
      tabcolor.title("COULORS")
def setting(): 
      global parametrefenetre
      parametrefenetre = Toplevel(fenetre)
      parametrefenetre.title("SETTING")
      choixcouleur = Button(parametrefenetre, text="Color",font=("arial",20), command= color)
      choixcouleur.pack(side="bottom", padx=20, pady=20)
      parametrefenetre.mainloop()
def move_check(event):
    global tags,s,l,play
    item = canvas.find_closest(event.x, event.y)[0]  # Trouve l'objet le plus proche
    tag = canvas.gettags(item)# Récupère ses tags
    tags=int(tag[0][1:])
    s=move_possible(tags)[0]
    l=l_move(l,tags)
    if play!=0:
        move()

def setting():
      global parametrefenetre
      parametrefenetre = Toplevel(fenetre) #creation de la fenetre fille
      parametrefenetre.title("SETTING")
      boutoncouleur = Button(parametrefenetre, text="Color", font=("Arial",20), command=color)
      boutoncouleur.pack(side="bottom", padx=80, pady=80)




def color():
      palettecouleur = Toplevel(parametrefenetre) 
      palettecouleur.title("PALETTE DE COULEUR")
      bred = Button(palettecouleur, text="red")
      bred.pack(padx=60, pady=20)
      bblack = Button(palettecouleur, text="black")
      bblack.pack(padx=60, pady=20)
      bpurple = Button(palettecouleur, text="purple")
      bpurple.pack(padx=60, pady=20)


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

for i in range(4):
    for j in range(4):
        e+=1
        canvas.create_rectangle((j*largeur_case, i*hauteur_case),
                ((j+1)*largeur_case, (i+1)*hauteur_case), fill="grey",tags="a"+str(e))
        canvas.create_text(((j*largeur_case)+60, (i*hauteur_case)+60),text=str(e),font=("Arial", 60, "bold"),fill="black",tags="a"+str(e))
canvas.delete("a16")

b1=Button(fenetre2,text="nouvelle partie" ,font=("arial",10),command=move)
b4=Button(fenetre2,text="charger partie" ,font=("arial",10))
b2=Button(fenetre,text="Help" ,font=("arial",20))
b3=Button(fenetre,text="Quit" ,command= fenetre.destroy ,font=("arial",20))
canvas.grid(row=0,column=5,rowspan=5)
canvas2.grid(row=0,column=0,columnspan=3)
b2.grid(row=6,column=0)
b3.grid(row=6,column=10)
canvas2.create_window(200,200, window=b1)
canvas2.create_window(200,250, window=b4)
canvas.bind("<Button-1>", move_check)
creer_ondes()
animer()
parametre = Button(fenetre, text="Setting",font=("arial", 20),command=setting )
parametre.grid(row=6,column=5)
fenetre.mainloop() 

