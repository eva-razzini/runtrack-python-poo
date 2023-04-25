class Rectangle:
    def __init__(self):
        self.__longeur = 10
        self.__largeur = 5

    def get_longeur(self):
        return self.__longeur
    
    def set_longeur(self, nouvelle_longeur):
        self.__longeur = nouvelle_longeur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

rectangle = Rectangle()
print("valeur init longeur", rectangle.get_longeur())
rectangle.set_longeur(6)
print("nouvelle longeur", rectangle.get_longeur())
print("valeur init largeur", rectangle.get_largeur())
rectangle.set_largeur(3)
print("nouvelle largeur", rectangle.get_largeur())