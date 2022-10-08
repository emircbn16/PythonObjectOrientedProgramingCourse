sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1: Sayilar listesini 'while' ile ekrana yazdırın.

# i = 0
# while (i < len(sayilar)):
#      print(sayilar[i])
#      i += 1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.

# baslangic = int(input('Başlangıç: '))
# bitis = int(input('Bitiş: '))

# i = baslangic
# while i < bitis:
#     i += 1
#     if (i % 2 == 1):
#         print(f'Tek Sayı: {i}')

# print(i)

#  3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

# x = 100
# while x >= 0:
#     print(x)
#     x -= 1
# print('Bitti...')
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

# numbers = []
# i = 0
# while i < 5:
#     sayi = int(input('Sayı: '))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini 'urunler' listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun. 
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyiniz.

# urunler = []

# adet = int(input('Kaç Tane Ürün İstiyorsunuz: '))
# i = 0

# while ( i < adet):
#     name = input('Ürün İsmi: ')
#     price = input('Ürün Fiyatı: ')
#     urunler.append({
#         'name': name,
#         'price': price
#     })
#     i += 1
# for urun in urunler:
#     print(f'Ürün Adı : {urun["name"]} Ürün Fiyatı : {urun["price"]}')