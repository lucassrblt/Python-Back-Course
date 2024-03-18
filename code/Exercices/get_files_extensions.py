# Objectif récupérer l'extensions d'un fichier et gérer les cas d'erreurs
# Pour compléter utiliser le module OS

extensions = {
    "png" : "Image",
    "jpg" : "Image",
    "jpeg" : "Image",
    "gif" : "Image",
    "mp3" : "Audio",
    "wav" : "Audio",
    "mp4" : "Vidéo",
    "avi" : "Vidéo",
    "mov" : "Vidéo",
    "pdf" : "Document",
    "doc" : "Document",
    "docx" : "Document",
    "txt" : "Document",
    "py" : "Code",
    "html" : "Code",
    "css" : "Code",
    "xls" : "Tableur",
    "xlsx" : "Tableur",
    "csv" : "Tableur",
}
def get_extension(file):
    extension = file.split(".") # Renvoie une array de forme ['chemin', 'extension']
    print(extension)
    if len(extension) > 1:
        file_type = extensions.get(extension[len(extension) - 1]) # Récupère la dernière valeur de l'array
        file_name = extension[0]
        if(file_type):
            print(f"Le ficheir reçu est {file_name} de type {file_type}")
        else:
            print("Extensions non reconnu")
    else:
        print("Pas d'extension détécté")

user_file = input("Entrez le chemin du fichier : ")
get_extension(user_file)


