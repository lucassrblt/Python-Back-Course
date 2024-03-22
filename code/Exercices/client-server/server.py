import socket
from squeal import *

socket_server = socket.socket()

socket_server.bind((socket.gethostname(), 3333))

socket_server.listen(5)

while True:
    client, adress = socket_server.accept()

    print(f"[LOG] Connexion entrante de {adress}")

    message = client.recv(1024)
    texte = message.decode()
    texte = transform_str(texte)

    squeal = get_squeal(texte.lower())

    if squeal:
        message = f"Le cri est {squeal}"
    else:
        message = "Animal inconnu"

    client.send(message.encode())
    client.close

