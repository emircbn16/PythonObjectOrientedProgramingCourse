# Inheritance (Kalıtım): Miras Alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a Person.')

    def eat(self):
        print('I am Eating.')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created.')
    # override
    def who_am_i(self):
        print('I am a Student.')
    
    def sayHello(self):
        print('Hello I am a Student.')
class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    def who_am_i(self):
        print(f'I am a {self.branch} Teacher.')

p1 = Person('Emir','Çoban')
s1 = Student('Nuri','Ersezer', 1279)
t1 = Teacher('Fatma','Yılbat','Eng.')

t1.who_am_i()
print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()

s1.sayHello()

p1.eat()
s1.eat()