from random import *

class JeuDeCartes:
  def __init__(self):
    self.l = []
    for j in range(4):
      for i in range(2,15):
        self.l = self.l + [(i, j)]

  def afficher(self):
    print(self.l, len(self.l))


  def nom_carte(self, j, i):
    if i == 0:
      a = "Coeur"
    elif i == 1:
      a = "Carreau"
    elif i == 2:
      a = "Trefle"
    elif i == 3:
      a = "Pique"
    else:
      return None
    if j == 11:
      b = "Valet"
    elif j == 12:
      b = "Dame"
    elif j == 13:
      b = "Roi"
    elif j == 14:
      b = "As"
    else:
      b = j
    return str(b) + " de " + str(a)

  def battre(self):
      l = []
      for i in range (len(self.l)):
          r = randint(0, len(self.l)-1)
          l.append(self.l[r])
          self.l.pop(r)
      self.l = l
      return self.l

  def tirer(self):
      if len(self.l) > 0:
          return self.l.pop(0)
      return None

A = JeuDeCartes()
B = JeuDeCartes()


def jeu():
    n = 52
    ap = 0
    bp = 0
    A.battre()
    B.battre()
    for i in range(n):
        a = A.tirer()[0]
        b = B.tirer()[0]
        #print(a, b) #verification
        if a > b:
            ap += 1
            #print("ap", ap) #verification
        elif b > a:
            bp += 1
            #print("bp", bp) #verification
        elif a == b:
            n +=1
    if ap > bp:
        print("Le joueur A est gagnant")
    else:
        print("Le joueur B est gagnant")

