import pandas as pd

#df = pd.read_csv("./Pandas_Learning/pokemon_data.csv")

#print(df.head(3)) #first 3 rows

#print(df.tail(3)) # last 3 rows

#df_xlsx = pd.read_excel("./Pandas_Learning/pokemon_data.xlsx") #able to read excel after installing openpyxl

#print(df_xlsx.head(3))

df = pd.read_csv("./Pandas_Learning/pokemon_data.csv", delimiter="/t")

print(df.head(5))