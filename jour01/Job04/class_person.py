class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("je suis ", self.prenom, self.nom)


personne = Personne("Doe", "John")
personne.SePresenter()
personne = Personne("Dupond", "Jean")
personne.SePresenter()