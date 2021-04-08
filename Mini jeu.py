class Aliment:
    def __init__(self, nom, prix, point):
        self.nom = nom
        self.prix = prix
        self.point = point

    def acheter(self, perso):
        if perso.argent >= self.prix:
            print(self.nom + " achat possible")
            perso.argent = perso.argent - self.prix
        else:
            print("achat impossible")

class Perso:

    def __init__(self, prenom, poids, taille, argent, points_vie):
        self.prenom = prenom
        self.poids = poids
        self.taille = taille
        self.argent = argent
        self.points_vie = points_vie

    def nourrir(self, aliment):
        n = aliment.point
        if self.points_vie + n >= 0:
            self.points_vie = self.points_vie + n
            if n > 0:
                return self.poids - n * 1/100
            return self.poids + n * 1 / 100
        return "impossible de se nourrir"

    def sprint(self):
        self.points_vie = self.points_vie + 1
        self.points_vie = self.points_vie - (1 * 1 / 100)

    def IMC(self):
        if self.poids / self.taille **2 >= 18.5 and self.poids / self.taille **2 <= 25:
            return True, "L'IMC de", str(self.prenom), "est de", str(self.poids / self.taille **2), "."
        return False, "L'IMC de", str(self.prenom), "est de", str(self.poids / self.taille **2), "."

    def bonne_sante(self):
        if self.poids / self.taille **2 >= 18.5 and self.poids / self.taille **2 <= 25:
            return str(self.prenom), "est en bonne santé."
        return str(self.prenom), "n'est pas en bonne santé."

    def affichage(self):
        print(("{} pèse {} kg et mesure {} m. {} a {} euros et {} points de vie.").format(self.prenom, self.poids, self.taille, self.prenom, self.argent, self.argent, self.points_vie))


Morgane = Perso("Morgane", 50, 1.6, 5, 4)
Paul = Perso("Paul", 60, 1.8, 10, 2)

#Morgane.affichage()

#print(("Morgane pèse {} kg et mesure {} m. Morgane a {} euros et {} points de vie.").format(Morgane.poids, Morgane.taille, Morgane.argent, Morgane.argent, Morgane.points_vie))

#print(("Paul pèse {} kg et mesure {} m. Paul a {} euros et {} points de vie.").format(Paul.poids, Paul.taille, Paul.argent, Paul.argent, Paul.points_vie))

#print(Paul.IMC(), Paul.bonne_sante())

hamburger = Aliment("hamburger", 2, -3)
pomme = Aliment("pomme", 0.5, 1)
eau = Aliment("eau", 1, 1)

hamburger.acheter(Paul)
pomme.acheter(Paul)
eau.acheter(Paul)

Paul.nourrir(eau)
Paul.nourrir(pomme)
Paul.nourrir(hamburger)

paulp = Paul.points_vie
n = 0
while paulp < 4:
    n += 1
    paulp += 1

print(("Paul doit faire {} sprints.").format(n))


print(Paul.points_vie)





























