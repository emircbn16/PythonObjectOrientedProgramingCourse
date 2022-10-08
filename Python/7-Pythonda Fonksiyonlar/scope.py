# Global Scope
x = 'Global x'

def function():
    # Local Scope
    # x = 'Local x'
    print(x)

function()
print(x)

################

# GLobal
name = 'Emir'

def changeName(new_name):
    # Local
    global name
    name = new_name
    print(name)

changeName('Nuri')
print(name)

################

name = 'Global String'

def greeting():
    # name = 'Emir'

    def Hello():
        # name = 'Nuri'
        print('Hello '+ name)

    Hello()

greeting()

################

x = 50
def test():
    global x
    print(f'x : {x}')

    x = 100
    print(f'Changed x to {x}')

test()
print(x)