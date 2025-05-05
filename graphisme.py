from random import randint
from random import choice
from time import sleep
import tkinter as tk
#from taq import l_move

l=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def cherche(n,l): 
    """on cherche la ligne i et la colonne j de l'élément n dans la matrice l"""
    for i in range(4): # on commence par parcourir chaque ligne l'une après l'autre
        for j in range(4): # pour chaque ligne on controle les éléments de la colonne
            if l[i][j]==n: # on verrifie l'élément n recherché correspond à l'élément cible par le parcourts du tableau
                return i,j # on retourne la ligne i et la colonne j de l'élément n
         
"""
def create():
    global l
    for i in range(20000):
        n=randint(0,15)
        d=choice([0,1])
        coord_n=cherche(n,l)
        if coord_n[d]<3 and coord_n[d]>0:
            a=choice([1,-1])
        elif coord_n[d]==0:
            a=1
        elif coord_n[d]==3:
            a=-1
        if d==1:
            l[coord_n[0]][coord_n[1]],l[coord_n[0]][coord_n[1]+a]=l[coord_n[0]][coord_n[1]+a],l[coord_n[0]][coord_n[1]]
        if d==0:
            l[coord_n[0]][coord_n[1]],l[coord_n[0]+a][coord_n[1]]=l[coord_n[0]+a][coord_n[1]],l[coord_n[0]][coord_n[1]]    
    coord_zero=cherche(0,l) # Trouve la position de 0
    l[coord_zero[0]][coord_zero[1]],l[3][3]=l[3][3],0# on remet le 0 à la fin de la matrice
    
    print(l)
    return l
"""


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

            
def creation():
    """ Création d'une matrice 4x4 avec des valeurs de 1 à 15. La dernière case est toujours 0."""
    global l
    i=0
    e=2# nombre de permutations
    # Effectue des permutations aléatoires entre les cases de la matrice
    while i!=e:
        n=randint(0,15)
        l_move(l,n)
        i+=1
    #target=cherche(n,l)# trouve les coordonées de l'élément n qui sera choisi de manière aléatoire
    coord_zero=cherche(0,l) # Trouve la position de 0
    n1=l[coord_zero[0]][3]
    l_move(l,n1)
    zer=cherche(0,l)# Trouve la position de 0
    n2=l[3][zer[1]]
    l_move(l,n2)
    return l

def move_possible(n,tab):
    zéro=cherche(0,tab)# Trouve la position de 0
    target=cherche(n,tab)# Trouve la position de n
    # Vérifie si le mouvement est possible (même ligne ou même colonne)
    if zéro[0]==target[0]:
        return 1,1  # le premier 1 est pour le déplacement est possible et le deuxieme pour la colonne
    elif target[1]==zéro[1]:
        return 1,0  # le premier 1 est pour le déplacement est possible et le zéro pour la ligne
    else:
        return 0,0


