class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, long, larg):
        self.longeur = long
        self.largeur = larg

    def aire(self):
        print(self.longeur * self.largeur)
    
class Cercle(Forme):
    def aire(self, pi, rayon):
        print(pi * rayon * rayon)

F = Forme()
C = Cercle()
R = Rectangle(10,5)

R.aire()
C.aire(3.14, 6)