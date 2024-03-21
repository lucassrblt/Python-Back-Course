from .Adresse import Adresse

class Habitation():
    def __init__(self, type: enumerate, surface: int, etage: int, adresse: list[Adresse]):
        self.type = type
        self.surface = surface,
        self.etage = etage,
        self.adresse = adresse