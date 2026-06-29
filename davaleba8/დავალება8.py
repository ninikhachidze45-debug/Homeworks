# 1.

def fibo(n):
    if n <= 1:
        return n
    else:
        return (n - 1) + (n - 2)

n = int(input('Enter number: '))

for i in range(n):
    print(fibo(i), end = ' ')



# 2.

def func(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

a = input('\nEnter first string: ')
b = input('Enter second string: ')

if func(a, b):
    print('Anagrams')
else:
    print('Not anagrams')



# 3.

def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)


n = int(input('Enter number: '))

print(facto(n))



# 4.

def count(string, symbol):
    count = 0
    for char in string:
        if char == symbol:
            count += 1
    
    return count

string = input('Enter string: ')
symbol = input('Enter symbol: ')

print(count(string, symbol))
