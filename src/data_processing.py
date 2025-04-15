#  Fichier de lecture du CSV 
import pandas as pd

def load_data(filepath):
    # Fonction qui lit un fichier CSV
    df = pd.read_csv(filepath, sep=';')
    
    # print(df)
    # Retourne les données du fichier lu 
    return df