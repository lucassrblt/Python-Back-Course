# Itere de 1 à 100
for i in range(1, 101):
  # Créer la liste de résultat
  res = []
  # Multiple de 3
  if i % 3 == 0:
    res.append("Fizz")
  # Multiple de 5
  if i % 5 == 0:
    res.append("Buzz")
  # Autre nombre
  # Si res est vide (liste vide == falsy value)
  if not res:
    res.append(str(i))
  # Bonus
  if i % 10 == 9:
    res.append("bonus")
  
  # Affichage résultat
  print(" ".join(res))