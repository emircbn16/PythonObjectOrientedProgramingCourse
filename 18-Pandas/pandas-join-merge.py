import pandas as pd

# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ["Emir","Nuri","Sefa","Salih"],
#     'LastName': ["Çoban","Ergezen","Koçak","Ağgün"]
# }

# orders = {
#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
# }

# df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner")
# result = pd.merge(df_customers,df_orders,how="left")
# result = pd.merge(df_customers,df_orders,how="right")
# result = pd.merge(df_customers,df_orders,how="outer")

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Emir","Nuri","Sefa","Salih"],
    'LastName': ["Çoban","Ergezen","Koçak","Ağgün"]
}
customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Turan"]
}

df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirstName","LastName"])
df_customersB= pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])
result = pd.concat([df_customersA,df_customersB], axis = 1)

print(result)