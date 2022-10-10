'''
    ogrenciler = {
        '120': {
            'ad': 'Emir',
            'soyad': 'Çoban',
            'telefon': '531 000 00 01'
        },
        '125': {
            'ad': 'Fatma',
            'soyad': 'Yılbat',
            'telefon': '531 000 00 02'
        },
        '128': {
            'ad': 'Aslı'
            'soyad': 'Yılbat'
            'telefon': '531 000 00 03'
        },
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.

    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone,
# }

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone,
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone,
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone,
    }
})

print('*'*50)


ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")
