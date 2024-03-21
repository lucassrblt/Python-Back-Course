from .Habitation import Habitation
from .Adresse import Adresse

class Personne():
    def __init__(self, nom: str, prenom: str, age: int, sexe: enumerate, habitation: list[Habitation], adresse: list[Adresse]):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.habitation = habitation
        self.adresse = adresse
    
    def getPersonne(self):
        personne_dict = {
            "nom": self.nom,
            "prenom": self.prenom,
            "age": self.age,
            "sexe": self.sexe,
            "habitation": self.habitation,
            "adresse": self.adresse
        }
        return personne_dict
