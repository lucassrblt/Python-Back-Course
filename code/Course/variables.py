# Typage fort dynamiques
a = 2
a = "Bonjour"
a (1, 2, 3) # Tuple


# Possibilté de lui donné un type attendu 
prenom: str = "Lucas" 
prenom = 2 # Typage dynamique donc pas d'erreur


# Possibilité de faire des conversion de types 
a = 2 # Int
a = str(a) # Conversion en string

# Liste 
nombres = [1, 2, 3, 4, 5]
nombres2 = list(1, 2, 3, 4, 5) # Possibilité de déclarer une liste avec la classe list

nombres.append(6) # Ajoute un élément à la fin de la liste, impossible avec les tuples

# Tuples
nombres = (1, 2, 3, 4, 5) # Listes immuables
nombres2 = tuple(1, 2, 3, 4, 5) # Possibilité de déclarer une liste avec la classe list

# nombres.append(6) # Erreur

# Dictionnaires
dico = {'prenom': 'Lucas', 'nom': 'Rimbault'}
print(dico['prenom']) # Lucas

# Liste, Tuples, Dictionnaires valeurs ordonnées = Enregistrés dans l'ordre déclaré


# Set
diffculty = {'easy', 'medium', 'hard'}
print(diffculty) # {'easy', 'medium', 'hard'}
diffculty.add('very hard') # Ajoute l'élément add
diffculty.discard('easy') # Ajoute l'élément discard

# Les sets sont des valeurs non ordonnées