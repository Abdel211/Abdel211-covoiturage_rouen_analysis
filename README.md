#  Analyse des Trajets de Covoiturage from / To Rouen

Ce projet utilise des données Open source du gouvernement français afin de comprendre les comportements de mobilité autour de Rouen ( covoiturage).


## Objectifs du Projet

J'ai divisé mon travail en deux parties  :

### 1. Partie : Analyse de datas manuellement (Notebook)

Cette phase m’a permis de découvrir, comprendre et manipuler les données. 

Le travail consiste à : 

- Une Analyse initiale des données  fournies par le gouvernement

- Identifier les colones pertinentes à utiliser

- Filtrer les trajets liés à Rouen (ville de départ ou d’arrivée)

- Faire des calculs statistiques (moyennes, min/max .. )

- Visualisations  (histogrammes, courbes, heatmaps)

> Cette partie est disponible dans le notebook :  
> `Notebook/covoiturage_analysis.ipynb`


### 2. Phase d'Automatisation (Scripts Python)

Pour cette partie j’ai automatisé l’analyse avec des scripts Python.

- Téléchargement automatique des données depuis une URL ( à recupérer depuis le site du gouvernement : voir partie Données utilisés) 

- Génération de visualisations  (distances, durées)

- Génération de cartes de chaleur pour les points de départ et d’arrivée from / to Roeun 

- Sauvegarde des cartes de chaleur en local dans le folder outputs 


##  Structure du Projet

- `src/main.py` : Script principal .  
- `src/recup_data.py` : Télécharge les données depuis une URL.  
- `src/read_data.py` : Lit le fichier csv.  
- `src/visualisation.py` : Gère les fonctions utilisés pour plot les graphiques et cartes de chaleurs.  
- `src/test.py` : Script pour tester les différents use-case.  
- `Notebook/` : Folder qui contient notebook dans lequel j'ai analyser tout les données.  
- `datas/` : Folder dont lequel on stocke les fichiers `.csv` téléchargés en local .  
- `outputs/` : Folder qui contient les html des cartes de chaleurs.  
- `requirements.txt` : Liste des librairies Python nécessaires.  
- `.gitignore` : Exclut les fichiers inutiles à mettre dans le depot distant.  
- `.gitattributes` : Gestion des gros fichiers avec Git LFS (.csv).  
- `README.md` : Documentation.


## Utilisation

Avant de lancer le projet, merci d'installer les dépendances nécessaires avec la commande suivante :

```bash
pip install -r requirements.txt
```

###  1. Notebook 
 
Cette partie permet de visualiser l'analyse complète, les observations et les graphiques que j'ai réalisés sans automatisation.

Lancer Jupyter Notebook avec la commande suivante :

```bash
jupyter notebook
```
Puis naviguer vers le fichier :

> Notebook/covoiturage_analysis.ipynb

Cela vous permettra de visualiser :

- Les étapes d'analyse que j'ai suivis

- Les statistiques descriptives

- Des graphiques

- Mes observations et conclusions détaillées

### 2. Automatisation via python 

Le script principal `src/main.py` permet d’automatiser l’analyse complète à partir d’un lien vers un fichier .csv récupéré depuis le site du gouvernement.

**Commande general :**

```bash
python -m src.main <URL_DU_CSV> [nom_du_fichier.csv] [nom_carte_de_chaleur_depart.html] [nom_carte_de_chaleur_arrivee.html]

```
>Les paramètres entre crochets [] sont optionnels.

Exemple : 

```bash
python -m src.main https://www.data.gouv.fr/fr/datasets/r/fa7b5c60-87ad-47ac-9a95-35b9a8725f7c data.csv carte_dep.html carte_arr.html
```

#### Résultats attendus : 

- Dans datas/ : Le fichier .csv téléchargé
-  Graphiques s’affichent automatiquement
- Dans outputs/ : Les Cartes de chaleur  

#### Test  
Pour la partie test des differents use case : 

Le script `test.py` permet de tester les differents cas pour assuer le bon fonctionnement du projet. 

Pour executer ce script il  suffit  d'exécuter cette commande : 


```bash
python src/test.py

```
Ce script vérifie :

- Le téléchargement correct des données

- La bonne exécution de l'analyse automatisée avec différents nombre de param

- La génération des carte de chaleurs

## Données  utilisées : 
Lien vers la page du gouvernement : 

https://www.data.gouv.fr/fr/datasets/trajets-realises-en-covoiturage-registre-de-preuve-de-covoiturage/ 


> Pour récupérer l’URL d’un fichier .csv :
> Clic droit sur le lien du fichier .csv sur le site
> ![alt text](image.png)
> Cliquer sur : Copier le lien vers le fichier
> ![alt text](image-1.png)

## Auteur

Anka Soubaai Abdelmajid For CESI 
