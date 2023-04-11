import pandas as pd

df = pd.read_csv("./Pandas_Learning/pokemon_data.csv")

#print(df.describe()) #prints max, min, mean, etc


#print(df.sort_values("Name", ascending= False))

print(df.sort_values(["Type 1", "HP"], ascending=[1 , 0])) #1=ascending, 0=descending
