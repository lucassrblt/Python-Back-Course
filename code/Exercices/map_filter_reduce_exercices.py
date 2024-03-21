from functools import reduce


liste = [
    {"fname": 'Gojira', "lname": 'Dilbert', "group": 1, "mark": 10},
    {"fname": 'Murron', "lname": 'Morticia', "group": 2, "mark": 12},
    {"fname": 'Furiosa', "lname": 'Beetlejuice', "group": 1, "mark": 11},
    {"fname": 'Usagi', "lname": 'Draven', "group": 1, "mark": 19},
    {"fname": 'Chewbacca', "lname": 'Yoda', "group": 2, "mark": 8},
    {"fname": 'Murron', "lname": 'Spock', "group": 3, "mark": 5},
    {"fname": 'Leia', "lname": 'Murron', "group": 4, "mark": 15},
    {"fname": 'Jor-El', "lname": 'Fester', "group": 3, "mark": 6},
    {"fname": 'Tintin', "lname": 'Anakin', "group": 4, "mark": 9},
    {"fname": 'Beavis', "lname": 'Dagwood', "group": 2, "mark": 15},
]

# Objectif ajouter un +2 aux notes de tous les étudiants
def add_points(student):
    student['mark'] += 2
    if student['mark'] > 20:
        student['mark'] = 20
    return student
    
print('Exercice 1')
liste = map(lambda el: add_points(el), liste)



# Afficher les éleves ayant une note supérieur ou égale à 10
print('Exercice 2')
liste_3 = filter(lambda el: el['mark'] >= 10, liste)
liste_3 = list(liste_3)
print(liste_3)



# Afficher la meilleur note du groupe 1
print("- Point 4")
liste_5 = filter(lambda el: el["group"] == 1, liste)
liste_5 = map(lambda el: el["mark"], liste_5)
max_1 = reduce(lambda a, n: a if a > n else n, liste_5, 0)
# max_1 = max(*liste_5)
# max_1 = max(liste_5)
print(max_1)


# La moyenne de chaque groupe
print("- Point 5")
liste_6 = map(lambda el: (el["group"], el["mark"]), liste)
def reduce_1(acc, el):
  g, n = el # g-group, n-mark
  cle = f"groupe_{g}" # groupe_1
  if not cle in acc:
    acc[cle] = [0, 0]
  acc[cle][0] += n # Somme des notes
  acc[cle][1] += 1 # Count des notes
  return acc
dict_1 = reduce(reduce_1, liste_6, dict())
for cle in dict_1:
  print(f"{cle} : {dict_1[cle][0] / dict_1[cle][1]:.2f}")