from random import randint as ashkan
l=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
def cherche(n,l):
    for i in range(4):
        for j in range(4):
            if l[i][j]==n:
                return i,j
def creation():
    global l
    i=0
    e=ashkan(1,9)*10 + 1
    while i!=e:
        a=ashkan(0,3)
        b=ashkan(0,3)
        c=ashkan(0,3)
        d=ashkan(0,3)
        l[a][c],l[b][d]=l[b][d],l[a][c]
        i+=1
    f=cherche(0,l)
    l[f[0]][f[1]],l[3][3]=l[3][3],l[f[0]][f[1]]
    return l
def move_possible(n):
    a=cherche(0,l)
    b=cherche(n,l)
    if a[0]==b[0]:
        return 1,1
    elif a[1]==b[1]:
        return 1,0
    else:
        return 0,0

print(creation())
print(move_possible(15))