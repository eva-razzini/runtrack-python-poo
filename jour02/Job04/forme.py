class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, long, larg):
        self.longeur = long
        self.largeur = larg

    def aire(self):
        print(self.longeur * self.largeur)

F = Forme()
R = Rectangle(10,5)
R.aire()