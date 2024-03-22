# Importe le module socket
import socket

# Création du socket
socket_serveur = socket.socket()

# Préparation de configuration du socket
host = socket.gethostname() # localhost
port = 3333

# Association du socket au port
socket_serveur.bind((host, port))

# Lance l'écoute
socket_serveur.listen(5)

# Boucle infinie pour récupérer toutes les connexions
while True:
  try:
    # Attend la prochaine connexion
    client, adresse = socket_serveur.accept()

    # Log
    print(f"[LOG] Connexion entrante de {adresse}")

    # Réception du message du client
    message = client.recv(1024)
    texte = message.decode()
    print(f"[LOG] Message reçu du client : {texte}")

    # Construction du message
    message = f"J'ai bien reçu le message {texte}"

    # Conversion en bytes
    contenu = message.encode()

    # Envoi du message
    client.send(contenu)

    # Ferme la connexion avec le client
    client.close()

  # Gestion des erreurs
  except Exception as e:
    print("[ERREUR] {e}")