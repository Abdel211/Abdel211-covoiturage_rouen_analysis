# Fichier de plot des histogramme et de la carte de chaleur 
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

def plot_histogram(df, column, title, xlabel):
    # Taille de la figure 
    plt.figure(figsize=(10, 5))
    
    # Plot de l'histogramme avec 50 intervalles 
    sns.histplot(df[column], bins=50)
    
    # Titre et labels 
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Nombre de Trajets")
    
    # Show des graphes 
    plt.grid()
    plt.show()

def plot_heatmap(df, lat_column, lon_column, zoom_start=11, center_coords=(49.433331, 1.08333)):
    # Initialisation de la carte centrée sur Rouen 
    heat_map = folium.Map(location=center_coords, zoom_start=zoom_start)
    
    heat_data = df[[lat_column, lon_column]].dropna().values.tolist()   # On récupère les coordonnées des points à afficher dropna for the NaN values , values to get a tableau to list transforme tableau to list 

    # Génération de la Heatmap  avec un rayon de densité
    HeatMap(heat_data, radius=10, min_opacity=0.4).add_to(heat_map)

    print("\n")
    print(f"****************** Affichage de la Heatmap des trajets ******************")
    
    # Retourn e la carte de chaleur
    return heat_map