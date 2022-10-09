'''
1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('Sayı: '))
result = 
if result: (sayi > 0) and (sayi<=100)
    print(f'Sayı 0-100 Arasında ')
else:
    print('Sayı 0-100 Arasında Değil!!')
'''
'''
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input('Sayı: '))
if (sayi > 0):
    if (sayi % 2 == 0):
        print('Girilen Sayı Pozitif Çift Sayıdır.')
    else:
        print('Girilen Sayı Pozitif Ancak Sayı Tek.')
else:
    print('Girilen Sayı Negatiftir.')
'''
'''
3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'emircbn16.13@gmail.com'
password = 'abc123'

girilenEmail = input('Email:')
girilenPassword = input('Password:')

if (girilenEmail == email): 
    if (girilenPassword == password):
        print('Uygulamaya Giriş Başarılı.')
    else:
        print('Parola Hatalı')
else:
    print('E-posta Hatalı.')

'''
'''
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and (a > c):
    print('a En Büyük Sayıdır ')
elif (b > a) and (b > c):
    print('b En Büyük Sayıdır ')
elif (c > b) and (c > a):
    print('c En Büyük Sayıdır ') 
'''
'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
    b-) Finalden 70 alındığında ortalamanın önemi olmasın
vize1 = float(input('Vize 1: '))
vize2 = float(input('Vize 2: '))
final = float(input('Final: '))

ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
 
  result = (ortalama>=50) and (final>=50)
  result = (ortalama >=50) or (final>=70)
1.Durum

 if (ortalama>=50):
     if (final>=50):
         print(f'Öğrencinin Ortalaması : {ortalama} ve Geçme Durumu Başarılı')
     else:
         print(f'Öğrencinin Ortalaması : {ortalama} ve Geçme Durumu Başarısız. Finalden En Az 50 Almalısınız')
 else:
     print(f'Öğrencinin Ortalaması : {ortalama} ve Geçme Durumu Başarısız.')
2.Durum

if (ortalama >=50):
    print(f'Öğrencinin Ortalaması : {ortalama} ve Geçme Durumu Başarılı')
else:
    if (final>=70):
        print(f'Öğrencinin Ortalaması : {ortalama} ve Geçme Durumu Başarılı.Finalden En Az 70 Aldığınız İçin Geçtiniz')
    else:
        print(f'Öğrencinin Ortalaması : {ortalama} ve Geçme Durumu Başarısız.')
'''
'''
 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
    Formül: (Kilo / Boy Uzunluğunun Karesi)
    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
    0-18.4     => Zayıf
    18.5-24.9  => Normal
    25.0-29.9  => Fazla Kilolu
    30.0-34.9  => Şişman (Obez)

name = input('Adınız: ')
kg = float(input('Kilonuz: '))
hg = float(input('Boyunuz: '))

index = (kg) / (hg ** 2)


if (index >= 0) and (index <= 18.4):
    print(f'{name} Kilo indeksin: {index} ve Kilo Değerlendirmen Zayıf.')
elif (index > 18.4) and (index <= 24.9):
    print(f'{name} Kilo indeksin: {index} ve Kilo Değerlendirmen Normal.')
elif (index > 24.9) and (index <= 29.9):
    print(f'{name} Kilo indeksin: {index} ve Kilo Değerlendirmen Kilolu.')
elif (index >= 29.9) and (index <= 34.9):
    print(f'{name} Kilo indeksin: {index} ve Kilo Değerlendirmen Obez.')
else:
    print('Bilgileriniz Yanlıştır.')
'''