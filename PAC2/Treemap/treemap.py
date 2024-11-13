import pandas as pd
import matplotlib.pyplot as plt
import squarify  # for treemap visualization

df = pd.read_csv("world_population.csv")
# https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset

top_10_countries = df[df['Rank'] <= 10]

print(top_10_countries)

sizes = top_10_countries['2022 Population']  # Population sizes
labels = top_10_countries['Country/Territory'] + "\n" + (top_10_countries['2022 Population'] / 1e6).round(1).astype(str) + "M"

plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=plt.cm.viridis_r(sizes / sizes.max()), alpha=0.8)
plt.axis('off')
plt.title("Top 10 Countries by Population (Rank 1-10)")
plt.show()