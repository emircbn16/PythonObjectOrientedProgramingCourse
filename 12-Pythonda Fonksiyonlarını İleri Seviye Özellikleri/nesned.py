# def greeting(name):
#     print('Merhaba ', name)

# print(greeting('Emir'))
# print(greeting)

# sayHello = greeting
# del sayHello
# print(sayHello)

# encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)

# outer(10)
# inner_increment(10)


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Number Must Be an İnteger")

    if not number >= 0:
        raise ValueError("Number Must Be Zero oy Positive")

    def inner_fuctorial(number):
        if number <= 1:
            return 1
        return number * inner_fuctorial(number - 1)

    return inner_fuctorial(number)
try:
    print(factorial("2"))
except Exception as ex:
    print(ex)