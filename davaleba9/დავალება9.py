# 1.

int_list = [10, 20, 30, 40]

num = int(input('Enter number: '))

def func(num):
    
    int_list.append(num)
    return int_list

print(func(num))



# 2.

list1 = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]

def func(list):
    sum = 0
    for i in list:
        sum += i
    
    return sum

print('Sum =', func(list1))



# 3.

gl_str = 'Global'

def func():
    gl_str = 'Local'
    return gl_str

print(func())



# 4. 

num = int(input('Enter number: '))

def func(number):
    if number < 10:
        return number
    
    return number % 10 + func(number // 10)

print(func(num))



# 5.

string = input('Enter string: ')

def func(s):
    if len(s) == 1:
        return s
    return func(s[1:]) + s[0]

print(func(string))