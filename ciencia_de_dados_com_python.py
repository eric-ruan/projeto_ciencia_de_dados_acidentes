import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt

df = pd.read_csv('cat_acidentes.csv', sep=';')

df = df.dropna(subset=['latitude', 'longitude'], how='any')

mapa = folium.Map(location=[-30.1, -51.15], zoom_start = 11)
coordenadas = list(zip(df.latitude, df.longitude))
mapa_calor = HeatMap(coordenadas, radius=9, blur=10)
mapa.add_child(mapa_calor)

mapa = folium.Map(location=[-30.1, -51.15], zoom_start=11)
mapa_cluster = MarkerCluster(coordenadas)
mapa.add_child(mapa_cluster)

df['data'] = pd.to_datetime(df['data'])
df_ano = df['data'].dt.year.value_counts()

df_ano = df_ano.drop(2202)

plt.bar(df_ano.index, df_ano.values)

gradiente = df_ano/df_ano.max()
cores = plt.cm.Blues(gradiente)

plt.bar(df_ano.index, df_ano.values, color = cores)