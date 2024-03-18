# Objectif checker le nb d'execution de lancement de ce script à l'aide d'un fichier txt, et incrémenter ce nombre

content = ''
with open("../count.txt", 'r') as files:
    content = files.read()


with open('../count.txt', 'w') as files:
    if content.split('=')[0] != 'NB_EXECUTION':
        files.writelines('NB_EXECUTION=1')
    else:
        counter = content.split('=')[1]
        new_num = int(counter) + 1
        files.writelines(f'NB_EXECUTION={new_num}')