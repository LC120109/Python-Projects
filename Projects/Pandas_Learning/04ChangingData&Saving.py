import pandas as pd

df = pd.read_csv("./Pandas_Learning/pokemon_data.csv")

df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"] #adding one (inefficient way to add them)
df = df.drop(columns=["Total"]) #deleting columns

df["Total"] = df.iloc[:, 4:10].sum(axis=1) #efficient way to sum them


#rearranging Total to the left side
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

print(df.head(5)) 

df = df.sort_values(["Total"], ascending=False) #sorting to see the most powerful pokemon
print(df.head(5))

#saving

#df.to_csv("./Pandas_Learning/updated_pokemon.csv", index=False) #index=False --> doesn't print the index on the left side

#df.to_excel("./Pandas_Learning/updated_pokemon.xlsx", index=False) #in xlsx

df.to_csv("./Pandas_Learning/updated_pokemon.txt", index=False, sep="\t")