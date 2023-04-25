class Student:
    def __init__(self, nom, prenom, nbr_stud, credits, level):
        self.__nom = nom
        self.__prenom = prenom
        self.__nbr_stud = nbr_stud
        self.__nbr_credits = credits
        self.__level = level

 
    def add_credits(self, nouveau_credits):
        if nouveau_credits >= 0:
            self.__nbr_credits = self.__nbr_credits + nouveau_credits
            print("Le nombre de crédits de ", self.__nbr_credits, " points")

    def stdentEval(self):
        if self.__level >= 90:
            return("Excellent")
        elif self.__level >= 80:
            return("Très bien")
        elif self.__level >= 70:
            return("Bien")
        elif self.__level >= 60:
            return("Passable")
        else:
            return("insuffisant")

    def studentInfo(self):
        notes = self.stdentEval()
        print("Nom = ",self.__nom)
        print("Prénom = ",self.__prenom)
        print("id = ", self.__nbr_stud)
        print("Niveau = ", notes)

student = Student("Doe", "John", 145, 0, 74)
student.add_credits(10)
student.add_credits(10)
student.add_credits(10)
student.studentInfo()