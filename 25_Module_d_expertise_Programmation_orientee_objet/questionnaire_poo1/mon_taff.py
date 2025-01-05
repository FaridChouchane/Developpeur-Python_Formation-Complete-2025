class Question:
    
    def __init__(self, titre, choix, bonneReponse):
        self.titre = titre
        self.choix = choix
        self.bonneReponse = bonneReponse
        
    def poserQuestion(self):
        print(self.titre)
        print("")
        for index, i in enumerate(self.choix, 1):
            print(f"{index} -- {i}")
        print("")       
        print("votre réponse : ")
        print("")  
        
        choix = input("")
        
        if choix == self.bonneReponse:
            print("")
            print(f"Bravo ! - {choix} - est la bonne réponse !")
            print("")
            print("")
        else:
            print("")
            print(f"désolé, - {choix} -  n'est pas la bonne réponse ...")
            print("")


       
q1 = Question("quelle est la capital du vin ?", ("paris", "marseille", "bordeaux"), "bordeaux")
print("")
q2 = Question("quelle est le pays de la harissa ?", ("Tunisie", "anglettere", "allemagne"), "Tunisie")
print("")

print("")
q1.poserQuestion()
print("")
q2.poserQuestion()
print("")