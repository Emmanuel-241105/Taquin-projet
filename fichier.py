def sauvegarder(fi:str,grille:list,time=[0,0,0],score=0) :
    e=0
    file=open(fi,"w")
    flat_grille=[i for j in grille for i in j]
    while e!=len(flat_grille):
        if (e+1)==len(flat_grille):
            file.write(f"{str(flat_grille[e])}\n")
        else:
            file.write(f"{str(flat_grille[e])};")
        e+=1
    e=0
    while e!=len(time):
        if (e+1)==len(time):
            file.write(f"{str(time[e])}\n")
        else:
            file.write(f"{str(time[e])};")
        e+=1
    file.write(str(score))

    file.close()
def list_de_list(tab):
    a=[]
    b=[]
    for i in range(len(tab)):
        b.append(tab[i])
        if i%4==3 and i!=0:
            a.append(b)
            b=[]
    return a

    


def lecture(fi:str):
    dico={}
    tab=[]
    file=open(fi,"r")
    li=file.readline()
    while li!="":
        e=li.split(";")
        for i in e:
            tab.append(int(i))
        li=file.readline()
    file.close()
    dico["liste"]=list_de_list(tab[:16])
    dico["time"]=tab[16:19]
    dico["score"]=tab[19:]
    return dico







