class Voiture:
    def __init__(self):
        self.__marque = "Mustang"
        self.__modele = "Ford mustang 2018"
        self.__annee = 2018
        self.__kilometrage = "120000"
        self.en_marche = False
        self.__reservoir = 50

    def demarrer(self):
        check_plein = self.__verifier_plein__()
        if self.en_marche == False and check_plein > 5 :
            print("La voiture à démarrer")
            self.en_marche = True
            return True
        else:
            print("La voiture n'a pas démarrer")
        
    def arreter(self):
        if self.en_marche == True:
            print("La voiture c'est arrêter")
            return False
        
    def __verifier_plein__(self):
        return self.__reservoir
    
    def get_marque(self):
        return self.__marque
    
    def set_marque(self, nouveau_marque):
        self.__marque = nouveau_marque

    def get_modele(self):
        return self.__modele
    
    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee
    
    def set_annee(self, nouveau_annee):
        self.__annee = nouveau_annee

    def get_kilometrage(self):
        return self.__kilometrage
    
    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

voiture = Voiture()
voiture.demarrer()
voiture.arreter()
print("Marque : " , voiture.get_marque())
print("Modèle : ", voiture.get_modele())
print("Année : ", voiture.get_annee())
print("Kilométrage : ", voiture.get_kilometrage())
voiture.set_marque("Fiat")
voiture.set_modele("Fiat 500x")
voiture.set_annee("2015")
voiture.set_kilometrage("109000")
print("Marque : " , voiture.get_marque())
print("Modèle : ", voiture.get_modele())
print("Année : ", voiture.get_annee())
print("Kilométrage : ", voiture.get_kilometrage())