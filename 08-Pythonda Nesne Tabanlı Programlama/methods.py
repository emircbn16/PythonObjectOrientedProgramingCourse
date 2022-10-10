# # class
# class Person:
#     # class attributes
#     address = 'No İnformation'

#     # constructor (yapıcı metod)
#     def __init__(self, name, year):

#         # object attributes
#         self.name = name
#         self.year = year

#     # methods
#     def intro(self):
#         print('Hello There. I am ' + self.name)


#     def calculateAge(self):
#         return 2020 - self.year


# # object (instance)
# p1 = Person(name = 'Emir', year = 2001)
# p2 = Person(name = 'Nuri', year = 2002)

# p1.intro()
# p2.intro()

# print(f'Adım: {p1.name} Yaşım: {p1.calculateAge()}')
# print(f'ADım: {p2.name} Yaşım: {p2.calculateAge()}')


class Circle:
    # Class Object Attribute
    pi = 3.14
    
    def __init__(self, yaricap = 1):
        self.yaricap = yaricap
    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)

c1 = Circle()  # YariCap = 1
c2 = Circle(5)

print(f'c1 : Alan = {c1.alan_hesapla()} Çevre = {c1.cevre_hesapla()}')
print(f'c2 : Alan = {c2.alan_hesapla()} Çevre = {c2.cevre_hesapla()}')
