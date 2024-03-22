from .Habitation import Habitation

class Personne():
    def __init__(self, nom: str, prenom: str, age: int, sexe: enumerate, habitation: list[Habitation]):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.habitation = habitation
    
    def getPersonne(self):
        personne_dict = {
            "nom": self.nom,
            "prenom": self.prenom,
            "age": self.age,
            "sexe": self.sexe,
            "habitation": self.habitation,
        }
        return personne_dict
    
    def addHabitation(self, new_habitation):
        self.habitation.append(new_habitation)
        print(f"Voici la nouvelle liste d'habitations : {self.habitation}")

    def leaveHabitation(self, old_habitation):
        self.habitation = filter(lambda el: el != old_habitation, self.habitation)
        self.habitation = list(self.habitation)
        print(f"Voici la nouvelle liste d'habitations : {self.habitation}")

    def leaveVillage(self):
        self.habitation = [] 
        print(f"Voici la nouvelle liste d'habitations : {self.habitation}")


    def presentation(self):
        print(self.habitation)
        if(len(self.habitation) > 0):
            print(f"Bonjour je me nomme : {self.prenom + ' ' + self.nom}. \n Voici mes habitations : {self.habitation}")
        else: 
            print(f"Bonjour je me nomme : {self.prenom + ' ' + self.nom}. \n Je ne suis plus au village.")
    