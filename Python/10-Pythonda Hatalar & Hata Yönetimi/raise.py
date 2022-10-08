# x = 10

# if x > 5:
#     raise Exception("x 5 den Büyük Değer Alamaz.")

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola En Az 7 Karakter Olmalıdır.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Parola Küçük Harf İçermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Parola Büyük Harf İçermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parola Rakam İçermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("Parola Alpha Numeric Harf İçermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("Parola Boşluk İçermemelidir.")
#     else:
#         print("Geçerli Parola.")

# password = '12345678aA@'

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Geçerli Parola.")
# finally:
#     print("Validation Tamamlandı.")


# class Person:
#     def __init__(self,name,year):
#         if len(name) > 10:
#             raise Exception("Name Fazla Karakter İçeriyor.")
#         else:
#             self.name = name

# p = Person("Emirrrrrrrrrrrrrr",2001)