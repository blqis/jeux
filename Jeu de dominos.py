from random import randint


class Domino:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def get_A(self):
        return self.A

    def get_B(self):
        return self.B

    def set_A(self, A):
        self.A = A
    
    def set_B(self, B):
        self.B = B

    def valeurs(self):
        dico = {}
        dico[0] = Domino.get_A(self)
        dico[1] = Domino.get_B(self)
        return dico
    
    def Compatible(self, D):
        if(Domino.get_A(self) == Domino.get_A(D) or Domino.get_A(self) == Domino.get_B(D) or Domino.get_B(self) == Domino.get_A(D) or Domino.get_B(self) == Domino.get_B(D)):
            return True
        else: return False


def CreerJeu():
    l =  []
    j = 0

    for i in range (0, 7):
        j = i
        while(j<7):
            D = Domino(i, j)
            l.append(Domino.valeurs(D))
            j+=1

    return l


def AfficherMain(Main):
    print("\n\nListe :")
    print(Main)


def Piocher(Pioche):
    indice = randint(0, 27)
    Pioche.pop(indice)


def Distribuer(Jeu):
    joueur_1 = []
    joueur_2 = []

    for i in range(0,7):
        indice = randint(0, len(Jeu)-1)
        joueur_1.append(Jeu[indice])
        Jeu.pop(indice)
        indice = randint(0, len(Jeu)-1)
        joueur_2.append(Jeu[indice])
        Jeu.pop(indice)
        
    return joueur_1, joueur_2, Jeu



def Jouer(Main, domino, Pioche):
    for i in range (0, len(Main)):
        if(Domino.Compatible(Main[i], domino)):
            if(Domino.get_A(Main[i])==Domino.get_A(domino)):
                Domino.set_A(domino, Domino.get_B(Main[i]))

            elif(Domino.get_A(Main[i])==Domino.get_B(domino)):
                Domino.set_A(domino, Domino.get_A(Main[i]))

            elif(Domino.get_B(Main[i])==Domino.get_A(domino)):
                Domino.set_B(domino, Domino.get_B(Main[i]))
            
            elif(Domino.get_B(Main[i])==Domino.get_A(domino)):
                Domino.set_B(domino, Domino.get_A(Main[i]))
            Main.pop(i)
            
            return Main, domino, Pioche


    
    indice = randint(0, len(Pioche)-1)
    Main.append(Pioche[indice])
    Pioche.pop(indice)
    
    return Main, domino, Pioche

   





C = Domino(3, 6)
D = Domino(2, 3)


#print(Domino.get_A(D))
#print(D.A)


#print(Domino.valeurs(H))


#print(Domino.Compatible(C, D))




l = CreerJeu()
AfficherMain(l)
Piocher(l)
AfficherMain(l)

print("\n\n\n")

print(Distribuer(l))

