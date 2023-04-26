class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        return self.age

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouveauAge):
        self.age = nouveauAge

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("j'ai ",self.age, " ans")

class Professeur:
    def __init__(self):
        self.age = 40
        self.__matiereEnseignée = ""

    def enseigner(self):
        print("Le cours va commencer")

    def bojour(self):
        print("bonjour")

    def matière(self):
        self.__matiereEnseignée == "EPS"


p = Personne()
e = Eleve()
prof = Professeur()

e.afficherAge()
e.bonjour()
e.allerEnCours()
e.modifierAge(15)
e.afficherAge()
prof.bojour()
prof.enseigner()