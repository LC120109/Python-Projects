import pandas as pd

df = pd.read_csv("./Pandas_Learning/updated_pokemon.csv")

#print(df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")]) #filtering based on 2 conditions + And

#print(df.loc[(df["Type 1"] == "Grass") | (df["Type 2"] == "Poison")]) #| is an Or condition

new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & (df["HP"] > 70)]

new_df.reset_index(drop=True, inplace=True) #resetting the index & drop so the old index is removed

print(new_df)

#new_df.to_csv("./Pandas_Learning/filtered_pokemon.csv")
