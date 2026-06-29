# def func1(name):
#     print(f'hello, {name}')

# func1('nini')


# def calc(a, b, c):
#     total = a + b + c
#     return total
# print(calc(2, 3, 4))


# def calc_price(quantity, price_per_unit):
#     calc = quantity * price_per_unit
#     return calc

# print(calc_price(4, 20))


# def calc(*args):
#     total = sum(args)
#     return total

# print(calc(1, 24, 44, 37))



# def display(*args):
#     for i in (args):
#         print (i)
    
# info = (1, 2, 4)
# display(*info)



# def display(a, b, c):
#     for i in (a, b, c):
#         print(i)


# display(1, 2, 3)



# def greet(name = 'guest'):
#     print(f'hey, {name}')

# greet()
# greet('nini')


# def greet(name, message = 'hey'):
#     print(F'{message}, {name}')


# greet('nini')
# greet('nini', 'hello')
# greet(message = 'hi', name  = 'nika')


# def details(name, age, city):
#     print(f'Name: {name}, Age: {age}, City: {city}')

# info= {'name': 'nini', 'age': 20, 'city': 'surami'}
# details(**info)

# info= {'name': 'nini', 'age': 20, 'city': 'surami'}

# print(info)

# print(f'Name: {info['name']}')


# def func():
#     x = 10
#     print(x)

# func()

# y = 12

# def func2():
#     print(y)

# func2()





# Global variable
# value = 100


# # Enclosing function
# def outer_function():
#  value = 50 # Enclosing function's variable
#  # Nested function
#  def inner_function():
#    print("Inside inner function:", value) # Uses enclosing function's variable
#  inner_function()
# outer_function()
# print("Outside any function (global):", value) # Accesses global variable


# def apply(func, a, b):
#     print(func(a,b))

# apply()

# global_var = 5

# def func(x):
#     global global_var
#     global_var += x

#     return global_var


# print(func(2))


# def add(a, b):
#     print(a + b)


# add(2, 3)


# list1 = [1, 2, 3, 4, 5]
# list1.append(7)
# print(list1)
      

# sum = 0
# for i in str(1234):
#     sum += i
#     print(sum)





# num =input('enter: ')
 
# sum = 0
# for i in num:
#     i = int(i)
#     sum += i
#     print(sum)

# try:
#     def func(numbers):
#         if isinstance(numbers, list):
#             return reduce(lambda x, y: x * y, numbers)

# except:
#     raise TypeError
# print('Parameter must be a list')

# # print(func([1, 2, 3, 4, 5]))

# print(func(1))


# def func(numbers):
#     try:
#         if isinstance(numbers, list):
#              return reduce(lambda x, y: x * y, numbers)
#     except TypeError:
#         return 'Parameter must be a list'
    


# print(func((1, 2)))
# print(func([1, 2, 3, 4, 5]))





# try:
#     first = float(input("What is your first number? "))
#     second = float(input("What is your second number? "))
#     print(f"{first} divided by {second} is {first / second}")
# except ValueError:
#     print("You must enter a number")
# except ZeroDivisionError:
#     print("You can't divide by zero")
