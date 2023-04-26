class Rectangle:
    def __init__(self, long, large):
        self.__longeur = long
        self.__largeur = large

    def périmètre(self):
        print((self.__longeur + self.__largeur)*2)

    def surface(self):
        print(self.__longeur * self.__largeur)

    def get_longeur(self):
        return self.__longeur
    
    def set_longeur(self, nouv_longeur):
        self.__longeur = nouv_longeur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, nouv_largeur):
        self.__largeur = nouv_largeur

class Parallélépipède(Rectangle):
    def __init__(self, long, large, hauteur):
        super().__init__(long, large)
        self.hauteur = hauteur

    def volume(self,long, large, hauteur):
        print(long * large * hauteur)

para = Parallélépipède(10,5,30)
rectangle = Rectangle(10,5)

rectangle.périmètre()
rectangle.surface()
print(rectangle.get_longeur())
print(rectangle.get_largeur())
rectangle.set_longeur(25)
rectangle.set_largeur(10)
print(rectangle.get_longeur())
print(rectangle.get_largeur())
para.volume(10,5,6)
