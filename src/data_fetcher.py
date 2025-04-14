import os
import requests
from src.config import DATA_PATH

def download_data(url, filename="data.csv"):
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    local_path = os.path.join(DATA_PATH, filename)

    if not os.path.exists(local_path):
        print(f"[INFO] Téléchargement depuis : {url} ...")
        response = requests.get(url, verify=False)
        with open(local_path, 'wb') as f:
            f.write(response.content)
        print(f"[INFO] Données sauvegardées sous : {local_path}")
    else:
        print(f"[INFO] Fichier déjà présent : {local_path}")

    return local_path
