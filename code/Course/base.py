ma_var = input("prénom ?") #Récupère le prénom de l'utilisateur
if True: 
    print('Oui !') # Boucle basé sur l'identation



# Manipulation de chaines de caractères

phrase = "Bonjour, je m'appelle Lucas"
print(phrase[0]) # B
print(phrase[0:7]) # Bonjour
print(phrase[0:7:2]) # Bno
print(phrase[:7]) # 7 premiers caractères
print(phrase[-7:]) # 7 derniers caractères
# Attention charactère de droite exlue phrase[0:1] = B

print(f'La phrase est {phrase}') # La phrase est Bonjour, je m'appelle Lucas  

phrase.split(' ') # ['Bonjour,', 'je', "m'appelle", 'Lucas']
