import pandas as pd

df = pd.read_csv('other-data/production_data.csv', encoding='latin-1')
print(df.head())

# sort production data by production from highest to lowest and give the top 20
df = df.sort_values(by='Production', ascending=False)
print(df.head(20))

# create new dataframe with every row except the row that contains the world production value
country_df = df[df['Country'] != 'WORLD']

country_df = country_df.sort_values(by='Production', ascending=False)
print(country_df.head(20))

# check whether the production values add up to the world production value in the last row
print(country_df['Production'].sum())

# create a new column called share of world production and calculate the share of world production for each country
country_df['Share of World Production'] = country_df['Production'] / country_df['Production'].sum()
print(country_df.head(20))

# plot the share of world production for the top 50 countries

import matplotlib.pyplot as plt
plt.bar(country_df['Country'].head(50), country_df['Share of World Production'].head(50))
plt.xticks(rotation=90)
plt.show()

# plot the share of exports for the top 20 countries
country_df = country_df.sort_values(by='Exports', ascending=False)
country_df['Share of Exports'] = country_df['Exports'] / country_df['Exports'].sum()
plt.bar(country_df['Country'].head(20), country_df['Share of Exports'].head(20))
plt.xticks(rotation=90)
plt.show()