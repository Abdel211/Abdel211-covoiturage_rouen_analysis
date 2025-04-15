# Fichier de telechargement de données
import os
import requests
from src.config import datas_path   # Import du chemin de stockage des données à partir de config.py

# Fonction qui télécharger des données à partir d'une URL et les sauvegarde localement
def download_data(url, filename="data.csv"):

    # Verif si le dossier de stockage existe, sinon le créer
    if not os.path.exists(datas_path):
        os.makedirs(datas_path)

    # Constuction du Path ou le file sera stocké
    local_path = os.path.join(datas_path, filename)

    # Vérification si le fichier existe déjà
    if not os.path.exists(local_path):
        
        print(f"*********************** Téléchargement depuis : {url} ***********************")
        response = requests.get(url)
        
        # Sauvegarde du contenu téléchargé en mode binaire
        with open(local_path, 'wb') as data_file:
            data_file.write(response.content)
        
        print(f"**** Données sauvegardées sous : {local_path} ****")
    
    else:
        # Si fichier présent on fait qu'un print 
        print(f"****************** Fichier déjà présent : {local_path} ******************")

    # Retourne le chemin local du fichier téléchargé pour utilisation ultérieure
    return local_path
