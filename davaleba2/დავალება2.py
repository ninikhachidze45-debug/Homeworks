#1.
num_list=[44,23,11,8,20,56,33,55]
n=int(input('Enter a number:'))
if n in num_list:
    print('The number in list')
else:
    print('The number not in list')


#2.
n=int(input('Enter an integar:'))
if n%2==0:
    print('The number is even')
else:
    print('The number is odd')


#3.
str1='Paris'
str2=input('What is your favourite city?')
if str1==str2:
    print('Same object')
else:
    print('Different object')


#4.
num_list=[44,23,11,8,20,56,33,55]
n=int(input('Enter a number:'))
if n>num_list[2] and n<num_list[-1]:
    print('More than list elements')
else:
    if n==num_list[5]:
        print('Equal')
    else:
        print('None of the conditions were met')