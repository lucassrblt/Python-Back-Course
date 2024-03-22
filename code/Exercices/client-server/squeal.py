animaux_squeal = {
    "chien": "aboiement",
    "chat": "miaulement",
    "vache": "meuglement",
    "coq": "cocorico",
    "cheval": "hennissement",
    "mouton": "bêlement",
    "oiseau": "chant",
    "lion": "rugissement",
    "éléphant": "barissement",
    "grenouille": "coassement"
}


def transform_str(str):
    str = str.lower().lsp


def get_squeal(animal):
    return animaux_squeal.get(animal, False)