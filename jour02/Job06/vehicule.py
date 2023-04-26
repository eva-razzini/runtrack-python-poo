class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        print("Marque = ", self.marque)
        print("Model = ",self.modèle)
        print("Année = ",self.année)
        print("Prix = ",self.prix)

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self,marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.portes = 4

    def informationsVehicule(self):
        print("Marque = ", self.marque)
        print("Model = ",self.modèle)
        print("Année = ",self.année)
        print("Prix = ",self.prix)
        print("Nombre de portes = ",self.portes)    

    def demarrer(self):
        print("Attention, je demarre")    

class Moto(Vehicule):
    def __init__(self, marque, modèle, année, prix):
        super().__init__(marque, modèle, année, prix)
        self.roue = 2

    def informationsVehicule(self):
        print("Marque = ", self.marque)
        print("Model = ",self.modèle)
        print("Année = ",self.année)
        print("Prix = ",self.prix)
        print("Nombre de roue = ",self.roue)

    def demarrer(self):
        print("Je roule")


voiture = Voiture("Mercedes", "Classe A", "2020", "18500")
voiture.informationsVehicule()
voiture.demarrer()
moto = Moto("yamaha", "1200 Vmax", "1987", "4500")
moto.informationsVehicule()
moto.demarrer()