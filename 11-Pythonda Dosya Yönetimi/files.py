# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(soya_adi,dosya_erişme_modu)
# dosya_erişme_modu => Dosyayı hangi amaçla açtığımızı belirtir.
'''
    # "w": (Write) yazma modu. 
    #    ** Dosyayı konumda oluşturur.
    #    ** Dosya içeriğini siler ve yeniden ekleme yapar.

    # file = open("NewFile.txt","w")
    # file = open("C:/users/MURAT/desktop/NewFile.txt","w")
    # file.close()

    # file = open("NewFile.txt","w") # encoding='utf-8'
    # file.write("Emir Çoban")
    # file.close()
'''
'''
# "a": (Append) ekleme. 
#    ** Dosya konumda yoksa oluşturur.

# file = open("NewFile.txt","a")
# file.write("\nEmir Çoban\n")
# file.close()
'''
'''
# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# file = open("NewFile2.txt","x")
'''

# "r": (Read) okuma(varsayılan). Dosay konumda yoksa hata verir.