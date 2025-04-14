import sys
from src.data_fetcher import download_data
from src.data_processing import load_data
from src.visualisation import plot_histogram, plot_heatmap

def main():
    if len(sys.argv) < 2:
        print("Usage : python -m src.main <URL_DU_CSV> [nom_du_fichier.csv]")
        sys.exit(1)

    url = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) >= 3 else "data.csv"

    print("=== Téléchargement des données ===")
    csv_path = download_data(url, filename)

    print("=== Chargement des données ===")
    data = load_data(csv_path)

    print("=== Filtrage des trajets liés à Rouen ===")
    data_rouen = data[(data['journey_start_town'] == 'Rouen') | (data['journey_end_town'] == 'Rouen')]
    print(f"[INFO] {len(data_rouen)} trajets liés à Rouen")

    print("=== Analyse des distances ===")
    plot_histogram(data_rouen, 'journey_distance', 'Répartition des distances', 'Distance (mètres)')

    print("=== Analyse des durées ===")
    plot_histogram(data_rouen, 'journey_duration', 'Répartition des durées', 'Durée (minutes)')

    print("=== Heatmap des lieux de départ (hors Rouen) ===")
    dep_sans_rouen = data_rouen[data_rouen['journey_start_town'] != 'Rouen']
    heatmap_dep = plot_heatmap(dep_sans_rouen, 'journey_start_lat', 'journey_start_lon', "Carte de chaleur des départs vers Rouen")
    heatmap_dep.save("outputs/heatmap_depart_Rouen.html")

    print("=== Heatmap des lieux d'arrivée (hors Rouen) ===")
    arr_sans_rouen = data_rouen[data_rouen['journey_end_town'] != 'Rouen']
    heatmap_arr = plot_heatmap(arr_sans_rouen, 'journey_end_lat', 'journey_end_lon', "Carte de chaleur des arrivées depuis Rouen")
    heatmap_arr.save("outputs/heatmap_arrivee_Rouen.html")

    print("=== Fin du programme ===")

if __name__ == "__main__":
    main()
