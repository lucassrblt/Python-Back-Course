class Adresse():
    def __init__(self, numero, rue):
        self.numero = numero
        self.rue = rue

    def get_complete_adresse(self):
        print(f"J'habite au : {self.numero + ' ' + self.rue}")