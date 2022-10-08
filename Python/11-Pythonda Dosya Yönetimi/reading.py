# try:
#     file = open("NewFile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print('Dosya Okuma Hatası.')
# finally:
#     print('Dosya Kapandı.')
#     file.close()

file = open('NewFile.txt',"r")

# */*/*/*/*/ for dögüsü */*/*/*/*/

# for i in file:
    # print(i, end= " ")

# */*/*/*/*/ read() fonksiyonu */*/*/*/*/

# content1 = file.read()

# print("\nİçerik 1\n")
# print(content1)

# content2 = file.read()

# print("\nİçerik 2\n")
# print(content2)

# content = file.read(5)
# content = file.read(3)
# content = file.read(3)

# print(content)

# */*/*/*/*/ readline() fonksiyonu */*/*/*/*/

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# */*/*/*/*/ readlines() fonksiyonu */*/*/*/*/

# liste = file.readlines()
# print(liste[0])
# print(liste[1])
# print(liste[2])

file.close()