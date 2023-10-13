import pandas as pd
df= pd.read_csv ("c:/Users/esmee/OneDrive - Wageningen University & Research/Documenten/GitHub/Group18.github.io/listings.csv")
import matplotlib.pyplot as plt
#avg_prices = df.groupby("neighbourhood")["name"].mean()
#avg_prices.plot(kind='bar', color='skyblue')
#plt.title("Amount of AIRBNB's by neighbourhood")
#plt.ylabel("Average Amount of AIRBNB's")
#plt.xlabel("Neighbourhood")
#plt.xticks(rotation=45)
#plt.show()

#count_per_neighbourhood = df["neighbourhood"].value_counts()
#count_per_neighbourhood.plot(kind='bar', color= "skyblue")
#plt.title("Number of AirBnB Locations Per Neighbourhood")
#plt.ylabel("Number of Locations")
#plt.xlabel("Neighbourhood")
#plt.xticks(rotation=45)
#plt.show()

df= pd.read_csv("c:/Users/esmee/OneDrive - Wageningen University & Research/Documenten/GitHub/Group18.github.io/listings.csv")

plt.figure(figsize=(5,3))  
plt.scatter(df['longitude'], df['latitude'], alpha=0.3, edgecolors="Orchid", linewidth=0.5, color = "hotpink")
plt.title("Scatter plot of Latitudes and Longitudes")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()
