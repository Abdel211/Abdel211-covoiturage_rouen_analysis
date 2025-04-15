# Fichier de test qui permet de tester le bon fonctionnement du script principal src/main.py
import subprocess
import os

def run_command(command):
    print(f" Commande exécutée : {command}")
    result = subprocess.run(command, shell=True)
    print(" Résultat :", result)

# Test sans arg
print("TEST 1 : Lancement sans arguments (doit afficher un message d'erreur)")
run_command("python -m src.main")

# Test avec url uniquement
print("TEST 2 : Lancement avec URL uniquement (doit créer data.csv par défaut)")
run_command("python -m src.main https://www.data.gouv.fr/fr/datasets/r/fa7b5c60-87ad-47ac-9a95-35b9a8725f7c")

# Test avec url + nom de fichier CSV
print("TEST 3 : Lancement avec nom de fichier CSV personnalisé")
run_command("python -m src.main https://www.data.gouv.fr/fr/datasets/r/fa7b5c60-87ad-47ac-9a95-35b9a8725f7c mars_2025.csv")

# Test avec tout les arguements 
print("TEST 4 : Lancement complet avec heatmanom de cartes de chaleurs personnalisées")
run_command("python -m src.main https://www.data.gouv.fr/fr/datasets/r/fa7b5c60-87ad-47ac-9a95-35b9a8725f7c mars_2025_test_2.csv carte_chaleur_depart_test.html carte_chaleur_Arrivé_test.html")

# Verification de la generation des html 
print("Vérification des fichiers générés dans outputs/")
print(os.listdir("outputs"))
