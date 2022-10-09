                                
                                    #SAYI TAHMİN OYUNU BÖLÜM 3


from random import randint


def  tahmin_sayısı_pc_pc(üst_sınır):
    print(f'A:Tahmin Ettiğim Sayı 1 ile {üst_sınır} Arasında')
    cevap = randint(1, üst_sınır)
    alt = 1
    üst = üst_sınır
    tahmin = None
    TahminSayisi = 0

    while tahmin != cevap:
        TahminSayisi += 1
        tahmin = (alt + üst ) // 2
        print(f'\nB:Tahminin {tahmin} mi ?!')
        if cevap > tahmin:
            print('A:Tahminim Daha Büyük')
            alt = tahmin + 1
        elif cevap < tahmin:
            print('A:Tahminim Daha Küçük')
            üst = tahmin - 1
        else:
            print('\nDoğru Cevap Reis')

    print(f'\n{TahminSayisi} Denemede Tahmin Ettin\n')


if __name__ == '__main__':
    tahmin_sayısı_pc_pc(10)