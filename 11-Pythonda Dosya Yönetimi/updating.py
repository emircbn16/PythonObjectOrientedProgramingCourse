# with open("NewFile.txt","r+") as file:
#     file.seek(40)
#     file.write("Deneme")

# with open("NewFile.txt","r+") as file:
#     print(file.read())

# */*/*/*/*/ Sayfa Sonuna Güncelleme*/*/*/*/*/

# with open("NewFile.txt","a") as file:
#     file.write("\nFatma Yılbat")

# */*/*/*/*/ Sayfa Başında Güncelleme*/*/*/*/*/

# with open("NewFile.txt","r+") as file:
#     content = file.read()
#     content = "Asli Yilbat\n" + content
#     file.seek(0)
#     file.write(content)

# */*/*/*/*/ Sayfa Ortasında Güncelleme*/*/*/*/*/

with open("NewFile.txt","r+") as file:
    list = file.readlines()
    list.insert(1,"Yilmaz Aygün\n")
    file.seek(0)
    file.writelines(list)

with open("NewFile.txt","r") as file:
    print(file.read())