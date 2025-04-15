# Code Principal 

import sys
# Import de toute les fonctions 
from src.data_fetcher import download_data
from src.data_processing import load_data
from src.visualisation import plot_histogram, plot_heatmap

# Code principak
def main():
    
    # Vérification des arguments de la ligne de commande 
    if len(sys.argv) < 2:
        print(" L'URL du fichier CSV est requise en argument.")
        sys.exit(1)

    # Récupération de l'URL à partir des arguments de la ligne de commande
    url = sys.argv[1]
    
    # Récupération du nom du fichier csv à partir de la ligne de commande si pas passé je donne data.csv comme non par défaut 
    filename = sys.argv[2] if len(sys.argv) >= 3 else "data.csv"

    # Recuperation du nom souhaité pour la heatmap départ et arrivée
    carte_chaleur_depart_name = sys.argv[3] if len(sys.argv) >= 4 else "carte_chaleur_to_Rouen.html"  # Nom heatmap départ
    carte_chaleur_arrivee_name = sys.argv[4] if len(sys.argv) >= 5 else "carte_chaleur_from_Rouen.html"  # Nom heatmap arrivée


    # Step 1 : Téléchargement des données
    
    print("****************** Téléchargement des données ******************")
    
    # téléchargement +  retour du chemin local du csv 
    csv_path = download_data(url, filename)

    # Step 2 : Chargement des données
    
    print("****************** Chargement des données ******************")
    
    # Lecture du CSV et retour du tableau de données 
    data = load_data(csv_path)

    # Step 3 : Filtrage des trajets liés à Rouen
    
    print("****************** Filtrage des trajets liés à Rouen ******************")
    
    # Je garde que les trajets qui ont comme point depart ou d'arrivée Rouen
    data_rouen = data[(data['journey_start_town'] == 'Rouen') | (data['journey_end_town'] == 'Rouen')]
    
    # Print du nbr de trajets from / to Rouen 
    print(f"---------------->  {len(data_rouen)} trajets liés à Rouen")

    # Step 4 : Plot de l'histogramme des distances 
    
    print("****************** Analyse des distances ******************")
    plot_histogram(data_rouen, 'journey_distance', 'Répartition des distances', 'Distance (mètres)')

    # Step 5 : Plot de l'histogramme des durées 
    
    print("****************** Analyse des durées ******************")
    plot_histogram(data_rouen, 'journey_duration', 'Répartition des durées', 'Durée (minutes)')

    # Step 6 : Plot de la carte de chaleur des lieux de départ
    
    print("****************** Heatmap des lieux de départ ******************")
    
    # Filtrage des villes de depart , enlever Rouen pour voir les deplacements inter-ville 
    dep_sans_rouen = data_rouen[data_rouen['journey_start_town'] != 'Rouen']
    
    # On plot la carte de chaleur en utilisant les coordonnées de départ des trajets (lat/lon)
    heatmap_dep = plot_heatmap(dep_sans_rouen, 'journey_start_lat', 'journey_start_lon', "Carte de chaleur des départs vers Rouen")
    
    # Save la carte de chaleur sous forme HTML 
    heatmap_dep.save(f"outputs/{carte_chaleur_depart_name}")

    # Step 7 : Plot de la carte de chaleur des lieux d'arrivée
    print("****************** Heatmap des lieux d'arrivée ******************")
    
    # Filtrage des villes d'arrivée , enlever Rouen pour voir les deplacements inter-ville 
    arr_sans_rouen = data_rouen[data_rouen['journey_end_town'] != 'Rouen']
    
    # On plot la carte de chaleur en utilisant les coordonnées d'arrivée des trajets (lat/lon)
    heatmap_arr = plot_heatmap(arr_sans_rouen, 'journey_end_lat', 'journey_end_lon', "Carte de chaleur des arrivées depuis Rouen")
    
    # Save la carte de chaleur sous forme HTML 
    heatmap_arr.save(f"outputs/{carte_chaleur_arrivee_name}")


    print("****************** Fin du programme ******************")

if __name__ == "__main__":
    main()
