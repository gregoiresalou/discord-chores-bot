import os 
import requests

URL = "WEBHOOK_URL"

def planing_nas():
    person = ["Marc", "Juliette", "Antonia", "Marta", "Grégoire"]
    dossier_actuel = os.path.dirname(os.path.abspath(__file__))
    fichier_memoire = os.path.join(dossier_actuel, "memoire.txt")

    if os.path.exists(fichier_memoire):
        with open(fichier_memoire, "r",encoding="UTF-8") as file:
            contenu = file.read()
            i = int(contenu)
    else :
        i = 0 #Si le fichier n'existe pas, on donne la valeur de 0 à i

    message = f"La personne qui doit nettoyer la cuisine est {person[i]}"
    donnee = {"content": message}
    requests.post(URL, json=donnee)
    

    if i == len(person) - 1: #Si i est égal à l'indice de la dernière personne dans la liste
        i = 0 
    else:
        i +=1 #Sinon on ajoute +1

    with open(fichier_memoire, "w") as file: 
        file.write(str(i)) #On écrit la valeur de i dans la mémoire pour la prochaine éxécution

planing_nas()



