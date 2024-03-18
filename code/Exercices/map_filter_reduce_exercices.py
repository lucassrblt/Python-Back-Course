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

def add_points(student):
    student['mark'] += 2
    if student['mark'] > 20:
        student['mark'] = 20
    return student
    

# liste = map(lambda el: add_points(el), liste)

# print(list(liste))


# Afficher les éleves ayant une note supérieur ou égale à 10
print(list(filter(lambda el: el['mark'] >= 10, liste)))


# Afficher la meilleur note du groupe 1
from functools import reduce
def best_marks_groups(best_marks, student):
    if student['group'] == 1:
        if best_marks == None or best_marks < student['mark']:
            best_marks = student['mark']
    return best_marks 

print(reduce(best_marks_groups, liste, None))


# Afficher la moyenne de chaque groupe



