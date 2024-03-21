prenom = input ("Quel est votre prénom ?")

if prenom.lower() == "lucas":
    print("Bonjour Lucas")
elif prenom.lower() == "jean":
    print("Bonjour Jean")
else:
    print("Bonjour inconnu")


# Ternaire 
is_first_name_defined = True if prenom else False


# Structure par cas 
match(prenom.lower()):
    case "lucas":
        print("Bonjour Lucas")
    case "jean":
        print("Bonjour Jean")
    case _: # Equivalent au default
        print("Bonjour inconnu")



# Boucles
        
while 2 == 2:
    print("Boucle infinie")



# Boucle for
prenoms = ("Damien", "Amina", "Renaud")
for prenom in prenoms:
  print(prenom)

# for (i = 0 ; i < 10 ; i++)
for i in range(10):
  print(i)

# for (i = 5 ; i < 15 ; i += 3)
for i in range(5, 15, 3):
  print(i)

# Dire 4 fois bonjour
for _ in range(4):
  print("Bonjour")

for i in range(10):
  # Passe au prochain élément
  if i % 2 == 0:
    continue # Passe à la prochaine occurence
  print(i)
  if i == 5:
    break # Sors d'une boucle