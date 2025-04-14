# src/visualisation.py

import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

def plot_histogram(df, column, title, xlabel):
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column], bins=50)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Nombre de Trajets")
    plt.grid()
    plt.show()

def plot_heatmap(df, lat_column, lon_column, map_title="Heatmap des trajets", zoom_start=11, center_coords=(49.433331, 1.08333)):
    """
    Crée une carte avec une heatmap des coordonnées fournies.
    """
    heat_map = folium.Map(location=center_coords, zoom_start=zoom_start)
    heat_data = df[[lat_column, lon_column]].dropna().values.tolist()

    HeatMap(heat_data, radius=10, min_opacity=0.4).add_to(heat_map)

    print(f"Affichage de la {map_title}")
    return heat_map
