# Import du module
import socket

# Création du socket
socket_client = socket.socket()

# Préparation de la configuration du serveur
host = socket.gethostname() # le hostname du serveur
port = 3333 # le port sur lequel le serveur écoute

# Connexion au serveur
socket_client.connect((host, port))

# Préparation du message
# contenu = b"Bla"
message = input("Enter un nom d'animal : ")
contenu = message.encode()

# Envoi du message au serveur
socket_client.send(contenu)

# Réception du message du serveur
message = socket_client.recv(1024)

# Conversion de bytes vers str
texte = message.decode()

# Affiche le message
print(f"{texte}")

# Ferme la connexion
socket_client.close()