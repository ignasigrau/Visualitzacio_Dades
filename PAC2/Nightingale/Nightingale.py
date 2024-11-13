import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("1990-2021.csv")
# https://www.kaggle.com/datasets/odins0n/monthly-gold-prices

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for the years 2019 and 2020
df = df[(df['Date'].dt.year == 2019) | (df['Date'].dt.year == 2020)]

# Extract month and year from the date for grouping
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Create separate datasets for 2019 and 2020
data_2019 = df[df['Year'] == 2019].sort_values(by='Month')
data_2020 = df[df['Year'] == 2020].sort_values(by='Month')

# Prepare the polar plot
fig, ax = plt.subplots(1, 1, figsize=(10, 10), subplot_kw=dict(polar=True))

# Define angles for each month (12 months, so divide 360 degrees into 12 parts)
angles = np.linspace(0, 2 * np.pi, 12, endpoint=False)

# Plot 2019 data
ax.bar(angles, data_2019['Europe(EUR)'], color='blue', alpha=0.6, width=0.3, label="2019", edgecolor="black")

# Plot 2020 data (shifted slightly for better comparison)
ax.bar(angles + 0.15, data_2020['Europe(EUR)'], color='orange', alpha=0.6, width=0.3, label="2020", edgecolor="black")

# Set labels for each month at corresponding angles
ax.set_xticks(angles)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], fontsize=12)

# Add legend and title
plt.legend(loc='upper right')
plt.title("Gold Price per Month (2019 vs 2020)")
plt.show()