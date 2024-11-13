import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.read_csv("USPopulations.csv")
# https://www.kaggle.com/datasets/bharxhav/us-city-populations-and-coordinates


plt.figure(figsize=(10, 8))
hb = plt.hexbin(df['LONG'], df['LAT'], C=df['2022_POPULATION'], gridsize=30,
                cmap='YlOrRd', reduce_C_function=np.sum, mincnt=1)

# Add color bar and labels
plt.colorbar(hb, label='Population in Bin')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Hexbin Plot of Population Density in USA by State")
plt.show()