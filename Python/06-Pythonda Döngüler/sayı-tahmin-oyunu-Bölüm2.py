
                                    #SAYI TAHMİN OYUNU BÖLÜM 2


import random

sayi = random.randrange(1,10)
tahmin = int(input("\n Aklınızdan 1 ile 10 Arasında Bi Sayı Tutunuz:"))

while tahmin != sayi:
    if tahmin < sayi:
        print("\n")
        tahmin = int(input("\n1 ile 10 Arasında bi Sayı Tahmin Ediniz: "))
    else:
        print("\nDaha Düşük Bir Tahmine İhtiyacınız Var.Tekrar Deneyiniz")
        tahmin = int(input("\n1 ile 10 Arasında bi Sayı Tahmin Ediniz: "))
    
print("\n Tebrikler Sayıyı Doğru Tahmin Ettiniz!\n")