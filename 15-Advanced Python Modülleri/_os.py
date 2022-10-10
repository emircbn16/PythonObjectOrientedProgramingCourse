import os 
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('..\..\..\..')

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.remove("yeniklasör/yeniklasör")

#listeleme
# result = os.listdir()
# result = os.listdir("C:\\")
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# ek dizin öğrenme
# result = os.getcwd()

# result = os.stat("_random.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("notepad.exe")

# path

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/Users/MURAT/Desktop/Python/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/Users/MURAT/Desktop/Python/_os1.py")
result = os.path.exists("C:/Users/MURAT/Desktop/Python/")
result = os.path.isdir("C:/Users/MURAT/Desktop/Python/")
result = os.path.isfile("C:/Users/MURAT/Desktop/Python/_os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
result = result[0]
result = result[1]

print(result)