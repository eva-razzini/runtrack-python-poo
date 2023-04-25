class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = " "

    def vieillir(self):
        print("L'âge de l'animal ", self.age, " ans")
        self.age = self.age + 1
        print("L'âge de l'animal ", self.age, " ans")

    def nommer(self, prenom):
       print("L'animal se nomme", prenom) 


animal = Animal()
animal.vieillir()
animal.nommer("Luna")

