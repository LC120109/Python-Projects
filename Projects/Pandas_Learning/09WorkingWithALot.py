import pandas as pd


df = pd.read_csv("./Pandas_Learning/updated_pokemon.csv")

new_df = pd.DataFrame(columns=df.columns)

#more detailed
for df in pd.read_csv("./Pandas_Learning/updated_pokemon.csv", chunksize=5): #only 5 rows at a time
    results = df.groupby(["Type 1"]).count()
    new_df = pd.concat([new_df, results])
    print(new_df)


