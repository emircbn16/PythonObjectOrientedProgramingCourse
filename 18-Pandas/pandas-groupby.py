import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Emir Çoban','Nurullah Ergezen','Sefa Koçak','Salih Ağgün','Işın Yücel','Rıza Ertürk','Mustafa Can'],
    'Departman': ['Application Developer','Application Developer','Muhasebe','İnsan Kaynakları','Web Designer','Muhasebe','İnsan Kaynakları'],
    'Yaş': [27,26,24,25,26,34,42],
    'Semt': ['Kadıköy','Kadıköy','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [6500,6500,4000,3500,5750,5500,4250]
}

df = pd.DataFrame(personeller)

result = df
result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

# for name, group in df.groupby("Semt"):
#     print(name)
#     print(group)

# for name, group in df.groupby("Departman"):
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Application Developer")
result = df.groupby("Departman").sum()
result = df.groupby("Departman").mean()
result = df.groupby("Departman")["Maaş"].mean()
result = df.groupby("Semt")["Yaş"].mean()
result = df.groupby("Semt")["Maaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()
result = df.groupby("Departman")["Yaş"].max()
result = df.groupby("Departman")["Maaş"].min()
result = df.groupby("Departman")["Maaş"].max()
result = df.groupby("Departman")["Maaş"].max()["Application Developer"]
result = df.groupby("Departman").agg(np.mean)
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Application Developer"]

print(result)