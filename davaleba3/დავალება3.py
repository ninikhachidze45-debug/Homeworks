# 1.
n = int(input('Enter a number: '))
sum = 0
for i in range(1, n):
    sum += i
print(sum)


# 2.
n = int(input('\nEnter a number: '))
while n > 0:
    print(n)
    n -= 1


# 3.
from random import randint
num = randint(1,100)
i = 1
guess = int(input(f'\nGuess a number between 1 and 100. Step #{i}: '))
while guess != num:
    i +=1
    print()
    if guess < num:
        print('Too low')
    else:
        print('Too high')
    guess = int(input(f'Try again. Step #{i}: '))
print('\nCorrect!')


# 4.
total_sum = 0
while True:
    user_input = input('\n\nEnter a number (type "sum" to finish): ')
    if user_input == "sum":
        break
    num = int(user_input)
    if num > 0:
        total_sum += num
print(total_sum)