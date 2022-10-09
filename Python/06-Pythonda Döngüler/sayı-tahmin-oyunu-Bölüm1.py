                                    
                                    #SAYI TAHMİN OYUNU BÖLÜM 1


import random

sayi = random.randint(1,10)
can = int(input('Kaç Hak Kullanmak İstersiniz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac} Seferde Bildiniz. Toplam Puanınız : {100 - (100 / can) * (sayac - 1)}')
        break
    elif sayi > tahmin:
        print('Sayıyı Arttırın.')
    else:
        print('Sayıyı Azaltın')
    if hak == 0:
        print(f'Hakkınız Bitti. Tutulan sayı : {sayi}')


