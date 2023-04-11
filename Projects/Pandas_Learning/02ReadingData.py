import pandas as pd

df = pd.read_csv("./Pandas_Learning/pokemon_data.csv")

#reading columns and specifics
#print(df.columns) #columns

#print(df["Name"])
#print(df.Name)
#print(df[["Name", "Type 1", "HP"]])

#reading rows and specifics

#print(df.iloc[1:4])

#print(df.iloc[2,1])
"""
for index, row in df.iterrows(): #read each row
    print(index, row)

for index, row in df.iterrows(): #read just name row
    print(index, row ["Name"])
"""

print(df.loc[df["Type 1"] == "Fire"]) #print specific data
