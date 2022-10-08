import pandas as pd
from numpy.random  import rand

df = pd.DataFrame(rand(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]


# loc["row",column] => loc["row"] => loc[":","column"]
result = df.loc["A"]
result = type(df.loc["A"])
result = df.iloc[2]
result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,"Column1":"Column2"]
result = df.loc[:,:"Column2"]
result = df.loc["A":"B",:"Column2"]
result = df.loc[:"B",:"Column2"]
result = df.loc["A","Column2"]
result = df.loc["C","Column1"]
result = df.loc[["A","B"],["Column1","Column2"]]
# print(result)

df["Column4"] = pd.Series(rand(3),["A","B","C"])
df["Column5"] = df["Column1"] + df["Column3"]

result = df.drop("Column5", axis = 1, inplace = True)



print(df)
