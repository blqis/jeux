T=      [[0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]


Tprimm=[[0,1,1,1,0,0,0],
        [1,3,3,4,3,2,1],
        [1,2,3,3,2,1,1],
        [1,2,3,3,3,2,1],
        [0,0,0,0,0,0,0]]



def voisines_vivantes(T,i,j):
    compteur=0
    for k in [i-1,i,i+1]:
        for l in [j-1,j,j+1]:
            try:
                compteur=compteur+T[k][l]
            except IndexError:
                compteur=compteur
    if T[i][j]==1:
        return compteur-1
    return compteur

def Tprim(T1):
    T3=[]
    for i in range(len(T1)):
        T2=[]
        for j in range(len(T1[0])):
            T2+=[voisines_vivantes(T1,i,j)]
        T3.append(T2)
    return T3

def tableau_zero(T):
    T3=[]
    for i in range(len(T)):
        T2=[]
        for j in range(len(T[0])):
            T2+=[0]
        T3.append(T2)
    return T3


def evolution(t):
    tprim=Tprim(t)
    P = tableau_zero(tprim)
    for i in range(len(tprim)):
        for j in range(len(tprim[0])):
            if tprim[i][j]==3 and t[i][j] == 0:
                P[i][j]=1
            elif tprim[i][j]==1:
                P[i][j]=0
            elif tprim[i][j]==4:
                P[i][j]=0
            elif t[i][j] == 1 and tprim[i][j]==2:
                P[i][j] = 1
            elif t[i][j] == 1 and tprim[i][j]==3:
                P[i][j] = 1

    return P
