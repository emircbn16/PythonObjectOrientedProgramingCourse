import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

bozulan_döviz = input("Bozulan Döviz Türü: ")
alinan_döviz = input("Alınan Döviz Türü: ")
miktar = int(input(f"Ne Kadar {bozulan_döviz} Bozdurmak İstiyorsunuz ? : "))

result = requests.get(api_url+bozulan_döviz)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_döviz, result["rates"][alinan_döviz], alinan_döviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_döviz, miktar * result["rates"][alinan_döviz], alinan_döviz))