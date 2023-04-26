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
        self.__matiereEnseignée = ""

    def enseigner(self):
        print("Le cours va commencer")

    def matière(self):
        self.__matiereEnseignée == "EPS"


p =Personne()
e = Eleve()
prof = Professeur()

e.afficherAge()
