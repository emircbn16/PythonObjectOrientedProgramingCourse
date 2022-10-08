#key - value

# 41 => kocaeli 34 => istanbul

# sehirler = ['kocaeli','istanbul']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('istanbul')])

#print(plakalar['kocaeli']) => 41
#print(plakalar['istanbul']) => 34

# plakalar = { 'kocaeli' : 41, 'istanbul' : 34 }

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

# plakalar['ankara'] = 6
# plakalar['kocaeli'] = 'new value'

# print(plakalar)

users = {
    'emircoban': {
        'age' : 19,
        'roles': ['admin','user'],
        'email': 'emir@gmail.com',
        'address': 'bursa',
        'phone':'1234569'
    },
    'fatmayilbat': {
        'age' : 25,
        'roles': ['user'],
        'email': 'fatma@gmail.com',
        'address': 'kayseri',
        'phone':'123456789'
    },
}
    
print(users['fatmayilbat']['roles'][0])


