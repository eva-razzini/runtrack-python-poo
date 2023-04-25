class Livre:
    def __init__(self):
        self.__titre = "Turbo"
        self.__auteur = "Eric Montaud"
        self.__nbr_pages = 5

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def get_nbr_pages(self):
        return self.__nbr_pages

    def set_nbr_pages(self, nouveau_nbr_pages):
        if nouveau_nbr_pages >= 0:
            self.__nbr_pages = nouveau_nbr_pages
        else:
            print("ERROR: enter un nombre de page entier positif")

livre = Livre()
print("valeur init titre", livre.get_titre())
livre.set_titre("Le chat bleu")
print("nouveau titre", livre.get_titre())
print("valeur init auteur", livre.get_auteur())
livre.set_auteur("Pascal Dumas")
print("nouveau auteur", livre.get_auteur())
print("valeur init nombres de pages", livre.get_nbr_pages())
livre.set_nbr_pages(3)
print("nouveau nombres de pages", livre.get_nbr_pages())
livre.set_nbr_pages(-7.5)
print("nouveau nombres de pages", livre.get_nbr_pages())