from random import randint as ashkan
from random import choice as balla
from time import sleep
import tkinter as tk

l=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def cherche(n,l): 
    """on cherche la ligne i et la colonne j de l'élément n dans la matrice l"""
    for i in range(4): # on commence par parcourir chaque ligne l'une après l'autre
        for j in range(4): # pour chaque ligne on controle les éléments de la colonne
            if l[i][j]==n: # on verrifie l'élément n recherché correspond à l'élément cible par le parcourts du tableau
                return i,j # on retourne la ligne i et la colonne j de l'élément n
            
def creation():
    """ Création d'une matrice 4x4 avec des valeurs de 1 à 15. La dernière case est toujours 0."""
    global l
    #target=cherche(n,l)# trouve les coordonées de l'élément n qui sera choisi de manière aléatoire
    coord_zero=cherche(0,l) # Trouve la position de 0
    l[coord_zero[0]][coord_zero[1]]=l[3][3]# on remet le 0 à la fin de la matrice
    l[3][3]=0 # l[x][y] designe l'élément de la ligne y et de la colonne x de la matrice l
    i=0
    e=20000# nombre de permutations
    # Effectue des permutations aléatoires entre les cases de la matrice
    while i!=e:
        n=ashkan(0,15)
        l_move(l,n)
        i+=1
    """coord_zero=cherche(0,l)
    n1=l[coord_zero[0]][3]
    n2=l[3][coord_zero[1]]
    l_move(l,n1)
    l_move(l,n2)""" # je voulais remettre la case vide à la position 3,3
   # print(cherche(0,l))
    return l

def move_possible(n):
    zéro=cherche(0,l)# Trouve la position de 0
    target=cherche(n,l)# Trouve la position de n
    # Vérifie si le mouvement est possible (même ligne ou même colonne)
    if zéro[0]==target[0]:
        return 1,1  # le premier 1 est pour le déplacement est possible et le deuxieme pour la colonne
    elif target[1]==zéro[1]:
        return 1,0  # le premier 1 est pour le déplacement est possible et le zéro pour la ligne
    else:
        return 0,0

def l_move(board,n): # bord c'est le tableau l et n c'est l'élément dont on veut savoir si le déplacement est possible
    move_possible_result=move_possible(n)
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
    
    # elif s[0]==1 and s[1]==1: # Si le mouvement est possible et concerne la colonne
    #     if b[1]>a[1]: # Si l'élément n est à droite de l'élément 0
    #         for i in range(abs(a[1]-b[1])): # Effectue le déplacement vers la droite
    #             l[a[0]][a[1]],l[a[0]][a[1]+1]=l[a[0]][a[1]+1],l[a[0]][a[1]]
    #             a=cherche(0,l)
    #         return l
    #     else: # Si l'élément n est à gauche de l'élément 0
    #         for i in range(abs(a[1]-b[1])): # Effectue le déplacement vers la gauche
    #             l[a[0]][a[1]],l[a[0]][a[1]-1]=l[a[0]][a[1]-1],l[a[0]][a[1]]
    #             a=cherche(0,l)
    #         return l
    # elif s[0]==1 and s[1]==0: # Si le mouvement est possible et concerne la ligne
    #     if b[0]>a[0]: # Si l'élément n est en dessous de l'élément 0
    #         for i in range(abs(a[0]-b[0])): # Effectue le déplacement vers le bas
    #             l[a[0]][a[1]],l[a[0]+1][a[1]]=l[a[0]+1][a[1]],l[a[0]][a[1]]
    #             a=cherche(0,l)
    #         return l
    #     else:
    #         for i in range(abs(a[0]-b[0])):
    #             l[a[0]][a[1]],l[a[0]-1][a[1]]=l[a[0]-1][a[1]],l[a[0]][a[1]]
    #             a=cherche(0,l)
    #         return l

