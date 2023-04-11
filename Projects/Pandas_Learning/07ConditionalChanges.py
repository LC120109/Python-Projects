import pandas as pd

df = pd.read_csv("./Pandas_Learning/updated_pokemon.csv")

#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = "Flamer" #changing Fire to Flamer

#print(df.loc[df["Type 1"] == "Flamer"])

#df.loc[df["Type 1"] == "Fire", "Legendary"] = True #changed all fire pokemons to legendary=True

#print(df.loc[df["Type 1"] == "Fire"])


df.loc[df["Total"] > 500, ["Generation", "Legendary"]] = "TEST VALUE" #changes both values if total over 500

print(df)