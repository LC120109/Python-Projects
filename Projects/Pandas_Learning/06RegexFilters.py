import pandas as pd
import re

df = pd.read_csv("./Pandas_Learning/updated_pokemon.csv")

#new_df = df.loc[df["Type 1"].str.contains("fire|grass",flags=re.I, regex=True)] #flags=ignore case

new_df = df.loc[df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)] #priting pokemons that start with Pi

print(new_df)