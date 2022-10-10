# class
class Person:
    # class attributes
    address = 'No İnformation'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('İnit Metodu Çalıştı.')

        # methods


# object (instance)
p1 = Person(name = 'Emir', year = 2001)
p2 = Person(name = 'Nuri', year =2002)

# updating
p1.name = 'Ahmet'
p1.address = 'İzmir'

# accesing object attributes
print(f'P1:Name: {p1.name} Year: {p1.year} Address: {p1.address}')
print(f'P2:Name: {p2.name} Year: {p2.year} Address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)