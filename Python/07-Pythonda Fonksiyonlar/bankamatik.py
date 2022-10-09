# Bankamatik Uygulaması

EmirHesap = {
    'Ad': 'Emir Çoban',
    'HesapNo': '127916',
    'Bakiye': 3000,
    'EkHesap': 2000
}

NuriHesap = {
    'Ad': 'Nurettin Ersezer',
    'HesapNo': '128113',
    'Bakiye': 2000,
    'EkHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['Ad']}")

    if (hesap['Bakiye'] >= miktar):
        hesap['Bakiye'] -= miktar
        print('Paranızı Alabilirsiniz.\n')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['Bakiye'] + hesap['EkHesap']
        
        if(toplam >= miktar):
            EkHesapKullanimi = input('Ek Hesap Kullanılsın Mı ? (E/H) :')

            if EkHesapKullanimi == 'E':
                EkHesapKullanilacakMiktar = miktar - hesap['Bakiye']
                hesap['Bakiye'] = 0
                hesap['EkHesap'] -= EkHesapKullanilacakMiktar
                print('Paranızı Çekebilirsiniz.')
                bakiyeSorgula(hesap)

            else:
                print(f"{hesap['HesapNo']} Nolu Hesabınızda {hesap['Bakiye']} Bulunmaktadır.")
        else:
            print('Üzgünüz.Yetersiz Bakiye\n')
            bakiyeSorgula(hesap)
def bakiyeSorgula(hesap):
    print(f"{hesap['HesapNo']} Nolu Hesabınızda {hesap['Bakiye']} TL Bulunmaktadır. Ek Hesap Limitiniz İse {hesap['EkHesap']} Tl dir ")

paraCek(EmirHesap, 1000)

print('************\n')

paraCek(EmirHesap, 2000)
