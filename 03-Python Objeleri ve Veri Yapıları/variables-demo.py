"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""
musteriAdi = 'Ali'
musteriSoyad = 'Yılmaz'
musteriAdSoyad = musteriAdi + ' ' + musteriSoyad
musteriCinsiyet = True #False
musteriTcKimlik = '12345678910'
musteriDogumYili = 1989
musteriAdresi = 'İstanbul Kadıköy'
musteriYasi = 2020 - musteriDogumYili

print(musteriAdi)
print(musteriSoyad)
print(musteriAdSoyad)
print(musteriCinsiyet)
print(musteriTcKimlik)
print(musteriDogumYili)
print(musteriAdresi)
print(musteriYasi)



"""
   2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
   sipariş 1 => 110    TL
   sipariş 2 => 1100.5 TL
   sipariş 3 => 356.95 TL
"""
order1 = 110
order2 = 1100.5
order3 = 356.95
total = order1 + order2 + order3

print("Total:",total)