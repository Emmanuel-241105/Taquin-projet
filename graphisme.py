from random import randint as ashkan
from random import choice as balla
from time import sleep
l=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
def cherche(n,l):
    for i in range(4):
        for j in range(4):
            if l[i][j]==n:
                return i,j
def creation():
    global l
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
    a=cherche(0,l)
    b=cherche(n,l)
    if b[0]==a[0]:
        return 1,1
    elif b[1]==a[1]:
        return 1,0
    else:
        return 0,0

def l_move(l,n):
    s=move_possible(n)
    a=cherche(0,l)
    b=cherche(n,l)
    if s[0]==0:
        return l
    elif s[0]==1 and s[1]==1:
        if b[1]>a[1]:
            for i in range(abs(a[1]-b[1])):
                l[a[0]][a[1]],l[a[0]][a[1]+1]=l[a[0]][a[1]+1],l[a[0]][a[1]]
                a=cherche(0,l)
            return l
        else:
            for i in range(abs(a[1]-b[1])):
                l[a[0]][a[1]],l[a[0]][a[1]-1]=l[a[0]][a[1]-1],l[a[0]][a[1]]
                a=cherche(0,l)
            return l
    elif s[0]==1 and s[1]==0:
        if b[0]>a[0]:
            for i in range(abs(a[0]-b[0])):
                l[a[0]][a[1]],l[a[0]+1][a[1]]=l[a[0]+1][a[1]],l[a[0]][a[1]]
                a=cherche(0,l)
            return l
        else:
            for i in range(abs(a[0]-b[0])):
                l[a[0]][a[1]],l[a[0]-1][a[1]]=l[a[0]-1][a[1]],l[a[0]][a[1]]
                a=cherche(0,l)
            return l
print(creation())
"""n=int(input("vas y"))
print (move_possible(n))
print(l_move(l,n))"""