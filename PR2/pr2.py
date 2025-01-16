import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics


# Càrrega de dades
data = pd.read_csv('spotify_tracks.csv')

mean_popularity = statistics.mean(data["popularity"])
print(mean_popularity)

# Popularitat al llarg dels anys
yearly_popularity = data.groupby('year')['popularity'].mean().reset_index()

# Gràfic de línies
plt.figure(figsize=(10, 6))
sns.lineplot(x='year', y='popularity', data=yearly_popularity, marker='o', color='blue')
plt.title('Evolució de la Popularitat al Llarg dels Anys')
plt.xlabel('Any de Llançament')
plt.ylabel('Popularitat Promig')
plt.grid(True)
plt.show()

# Gràfic de dispersió amb regressió
plt.figure(figsize=(10, 6))
sns.regplot(x='year', y='popularity', data=data, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.title('Correlació entre Any de Llançament i Popularitat')
plt.xlabel('Any de Llançament')
plt.ylabel('Popularitat')
plt.show()

# Filtrar cançons populars (popularitat > 80)
popular_songs = data[data['popularity'] > 80]

# Gràfic de violí per característiques musicals
plt.figure(figsize=(12, 6))
sns.violinplot(data=popular_songs[['acousticness', 'danceability', 'energy']], palette='muted')
plt.title('Distribució de Característiques Musicals (Cançons Populars)')
plt.ylabel('Valor')
plt.xticks([0, 1, 2], ['Acousticness', 'Danceability', 'Energy'])
plt.show()

# Gràfic de barres apilat per llengua
language_features = popular_songs.groupby('language')[['acousticness', 'danceability', 'energy']].mean()
language_features.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='coolwarm')
plt.title('Característiques Musicals per Llengua (Cançons Populars)')
plt.ylabel('Promig de Característiques')
plt.xlabel('Llengua')
plt.legend(title='Característica')
plt.show()

# Convertir duració a minuts
data['duration_min'] = data['duration_ms'] / 60000

# Histograma detallat de durades entre 0 i 10 minuts
plt.figure(figsize=(10, 6))
sns.histplot(data[data['duration_min'].between(0, 10)],
             x='duration_min',
             kde=True,
             bins=50,
             color='purple')
plt.title('Distribució de la Durada de les Cançons (0-10 minuts)')
plt.xlabel('Durada (Minuts)')
plt.ylabel('Comptatge')
plt.grid(True)
plt.show()

# Gràfic de dispersió
plt.figure(figsize=(10, 6))
sns.scatterplot(x='duration_min', y='popularity', data=data, alpha=0.5)
plt.title('Relació entre Durada i Popularitat')
plt.xlabel('Durada (Minuts)')
plt.ylabel('Popularitat')
plt.show()

# Gràfic de dispersió
plt.figure(figsize=(10, 6))
sns.scatterplot(x='liveness', y='popularity', data=data, alpha=0.5)
plt.title('Relació entre Liveness i Popularitat')
plt.xlabel('Liveness')
plt.ylabel('Popularitat')
plt.show()

data['liveness_bin'] = data['liveness'] > 0.5

# Crear el gràfic de barres
plt.figure(figsize=(8, 6))
sns.barplot(data=data, x='liveness_bin', y='popularity', ci=None, palette='Blues')

# Configurar títol i etiquetes
plt.title("Relació entre Popularitat i Liveness (True/False)", fontsize=16)
plt.xlabel("Liveness (True: >0.5, False: ≤0.5)", fontsize=12)
plt.ylabel("Mitjana de Popularitat", fontsize=12)

# Mostrar el gràfic
plt.tight_layout()
plt.show()

# Relació entre sonoritat i popularitat
plt.figure(figsize=(10, 6))
plt.scatter(data['loudness'], data['popularity'], alpha=0.5, color='blue')
plt.xlim(-20, 0)
plt.title("Relació entre Loudness i Popularitat (Rang -20 a 0)", fontsize=16)
plt.xlabel("Loudness (dB)", fontsize=12)
plt.ylabel("Popularitat", fontsize=12)
plt.tight_layout()
plt.show()

# Filtramos los valores de loudness para que estén entre -20 y 0
data_filtered = data[(data['loudness'] >= -20) & (data['loudness'] <= 0)]

# Crear bins para 'loudness' de -20 a 0 con intervalos de 2
loudness_bins = pd.cut(data_filtered['loudness'], bins=range(-20, 1, 2))  # Intervalos de 2 desde -20 a 0

# Crear bins para 'popularity' de 0 a 100 con intervalos de 10
popularity_bins = pd.cut(data_filtered['popularity'], bins=range(0, 101, 10))

# Crear una tabla de contingencia para el mapa de calor
heatmap_data = data_filtered.groupby([loudness_bins, popularity_bins])['popularity'].mean().unstack(fill_value=0)

# Mostrar el DataFrame generado para el heatmap
print(heatmap_data)

# Crear el heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.2f', cbar_kws={'label': 'Popularity'})
plt.title('Mapa de calor entre Loudness y Popularity')
plt.xlabel('Popularity')
plt.ylabel('Loudness')
plt.show()


