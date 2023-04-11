import pandas as pd

df = pd.read_csv("./Pandas_Learning/updated_pokemon.csv")

#using Groupby
#print(df.groupby(["Type 1"]).mean()) #mean doesn't work bc of the Pandas bug

#print(df.groupby(["Type 1"]).sum())


#just printing how many in each group
df["count"] = 1

print(df.groupby(["Type 1", "Type 2"]).count()["count"]) 

