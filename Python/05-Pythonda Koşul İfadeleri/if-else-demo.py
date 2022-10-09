# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#      durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 yaş ve eğitim durumu
#      lise ya da üniversite olmalıdır.

# isim = input('İsim: ')
# yas = int(input('Yaş: '))
# egitim = input('Eğitim Durumu (İlkOkul-Lise-Üniversite) : ')

# if (yas >= 18):
#     if (egitim == 'Lise' or egitim == 'Üniversite'):
#         print('Ehliyet Alınabilir')
#     else:
#         print('Ehliyet Alınamaz (Eğitim Durumu Yetersiz)')
# else:
#     print('Ehliyet Alınamaz (Yaşınız Tutmuyor)')

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

# yazili1 = float(input('1.Yazılı: '))
# yazili2 = float(input('2.Yazılı: '))
# sozlu = float(input('Sözlü: '))

# ortalama = (yazili1 + yazili2 + sozlu) / 3

# if (ortalama >= 0) and (ortalama < 25):
#     print(f'Ortalamanız: {ortalama} Notunuz : 0') 
# elif(ortalama >= 25) and (ortalama < 45):
#      print(f'Ortalamanız: {ortalama} Notunuz : 1') 
# elif(ortalama >= 45) and (ortalama < 55):
#      print(f'Ortalamanız: {ortalama} Notunuz : 2') 
# elif(ortalama >= 55) and (ortalama < 70):
#      print(f'Ortalamanız: {ortalama} Notunuz : 3') 
# elif(ortalama >= 70) and (ortalama < 85):
#      print(f'Ortalamanız: {ortalama} Notunuz : 4') 
# elif(ortalama >= 85) and (ortalama <= 100):
#      print(f'Ortalamanız: {ortalama} Notunuz : 5') 
# else:
#     print('Yanlış Bilgi Girdiniz')

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdaki bilgilere 
#    göre hesaplayınız.
#    1. Bakım => 1. Yıl
#    2. Bakım => 2. Yıl
#    3. Bakım => 3. Yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    *** datetime modülünü kullanmanız gerekiyor.
# !!!import datetime
# tarih = input('Aracınız Hangi Tarihte Trafiğe Çıktı (GG/AA/YYYY): ')
# tarih = tarih.split('/')
# trafigecikis = datetime.datetime(int(tarih[2]),int(tarih[1]),int(tarih[0]))
# simdi = datetime.datetime.now()
# fark = simdi - trafigecikis
# days = fark.days !!!

# if days <= 365:
#     print('1.Servis Aralığı')
# elif (days > 365) and (days <= 365 * 2):
#     print('2.Servis Aralığı')
# elif (days > 365 * 2) and (days <= 365 * 3):
#     print('3.Servis Aralığı')
# else:
#     print('Hatalı Süre Bilgisi')