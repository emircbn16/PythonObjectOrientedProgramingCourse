def sayHello(name = 'user'):
    return 'Hello  '+ name

msg = sayHello('Emir')
msg = sayHello('Ali')

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2020 - dogumYili

ageEmir = yasHesapla(2001)
ageAli = yasHesapla(1985)
print(ageEmir, ageAli)

def EmekliligeKacYİlKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum Yiliniza Gore Emekliliginize Kac Yil Kaldi.
    INPUT: Dogum Yili.
    OUTPUT: Hesaplanan Yil Bilgisi.
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı. ')
    else:
        print('Zaten Emekli Oldunuz.')

EmekliligeKacYİlKaldi(1985, 'Ali')

print(help(EmekliligeKacYİlKaldi))

list = [1,2,3,]
print(help(list.append))