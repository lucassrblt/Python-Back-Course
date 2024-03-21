# MAP (transform)
nombres = (range(5)) # (0, 1, 2, 3, 4)

nombres_carres = map(lambda n: n**2, nombres)
nombres_carres = tuple(nombres_carres)
print(nombres_carres)

# FILTER (séléctionner)
nombres = (range(10))
nombres_filtres = filter(lambda n: n%2==0, nombres)
nombres_filtres = tuple(nombres_filtres)
print(nombres_filtres)

# REDUCE
from functools import reduce
nombres = (range(10)) # Retourne une liste de 1 à 10
def calcul(acc, nb):
  return acc + nb
somme = reduce(calcul, nombres, 0)
print(somme)