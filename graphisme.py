from random import randint as ashkan
from random import choice as balla
from time import sleep
import tkinter as tk

l=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def cherche(n,l):
    for i in range(4):
        for j in range(4):
            if l[i][j]==n:
                return i,j
            
def creation():
    """ Création d'une matrice 4x4 avec des valeurs de 1 à 15. La dernière case est toujours 0."""
    global l
    coord_zero=cherche(0,l) # Trouve la position de 0
    l[coord_zero[0]][coord_zero[1]]=l[3][3]
    l[3][3]=0
    i=0
    e=196
    while i!=e:
        a=ashkan(0,3)
        b=ashkan(0,3)
        c=ashkan(0,3)
        d=ashkan(0,3)
        if l[a][c]!=0 and l[b][d]!=0:
            l[a][c],l[b][d]=l[b][d],l[a][c]
            i+=1
    print(cherche(0,l))
    return l

def move_possible(n):
    a=cherche(0,l)# Trouve la position de 0
    b=cherche(n,l)# Trouve la position de n
    # Vérifie si le mouvement est possible (même ligne ou même colonne)
    if a[0]==b[0]:
        return 1,1  # le premier 1 est pour le déplacement est possible et le deuxieme pour la colonne
    elif b[1]==a[1]:
        return 1,0  # le premier 1 est pour le déplacement est possible et le zéro pour la ligne
    else:
        return 0,0

def l_move(board,n):
    move_possible_result=move_possible(n)
    zero_position=cherche(0,board)#position du zéro
    target_position=cherche(n,board)# position de la case dont on veut déterminer si le déplacement est possible
    
    if move_possible_result[0]==0: # Si le mouvement n'est pas possible, retourne le board sans modification.
        return board, False
    
    # Détermine si le mouvement se fait sur la même ligne ou la même colonne
    # Calcul des déplacements
    row_difference = target_position[0] - zero_position[0]  # Différence de ligne
    column_difference = target_position[1] - zero_position[1]  # Déplacement sur les colonnes

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

