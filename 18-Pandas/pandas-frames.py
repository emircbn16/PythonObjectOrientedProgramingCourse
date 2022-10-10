import pandas as pd

file = [["Emir",50], ["Salih",60], ["Nuri",70], ["Sefa",80]]
dict = {"Name": ["Emir","Salih","Nuri","Sefa"],"Grade": [50,60,70,80]}
dict_list = [
                {"Name":"Emir","Grade":50},
                {"Name":"Salih","Grade":60},
                {"Name":"Nuri","Grade":70},
                {"Name":"Sefa","Grade":80},
            ]

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4,5])
# df = pd.DataFrame(data, columns = ['Name','Grade'], index = [1,2,3,4], dtype = float)
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index = ["1279","1281","1283","1285"])
df = pd.DataFrame(dict_list, index = ["1279","1281","1283","1285"])

print(df)

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1 , oranges = s2)

# df = pd.DataFrame(data)

# print(df)
