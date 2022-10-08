# def changeName(n):
#     n = 'Emir'

# name = 'Nuri'

# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'İstanbul'

# sehirler = ['Ankara','izmir']

# change(sehirler[:])

# print(sehirler)

def add(*params):
    print(type(params))
    sum = 0
    for n in params:
        sum = sum + n
    return sum

print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30, 50, 60, 10, 20))

def displayUserr(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUserr(name = 'Emir', age = 8, city = 'Bursa')
displayUserr(name = 'Nuri', age = 8, city = 'İzmir', phone = '123456')
displayUserr(name = 'Işın', age = 8, city = 'Ankara', phone ='123489', email = 'ışın@gmail.com')

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60 , 70, key1 = 'value 1', key2 = 'value 2')