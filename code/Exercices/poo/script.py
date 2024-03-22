from classes.Personne import Personne
from classes.Adresse import Adresse
from classes.Habitation import Habitation

adresse_1 = Adresse("40", "Voltaire")
habitation_1 = Habitation(0, 42, 1, adresse_1)

adresse_2 = Adresse("50", "Meunot")
habitation_2 = Habitation(1, 12, 1, adresse_2)

personne_1 = Personne('Personne', '1', 20, 1, [habitation_1])

personne_1.presentation()

