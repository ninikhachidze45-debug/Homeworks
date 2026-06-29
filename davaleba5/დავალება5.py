# 1.
list = []
while True:
    symbol = input('Enter "a", "r" or "e": ')
    if symbol == 'a':
        num = int(input('Enter number: '))
        list.append(num)
    elif symbol == 'r':
        num = int(input('Enter number: '))
        if num in list:
            list.remove(num)
        else:
            print('Number not in list')
    elif symbol == 'e':
        break
    else:
        print('Invalid symbol')
print('Final list:', list)


# 2.
my_list_1 = [43,'22', 12, 66, 210, ["hi"]]
print(my_list_1.index(210))
my_list_1[5].append('hello')
print(my_list_1)
my_list_1.pop(2)
print(my_list_1)
import copy 
my_list_2 = copy.deepcopy(my_list_1)
my_list_2.clear()
print( my_list_1, my_list_2)


# 3.
import re
phone = input('Enter phone number: ')
pattern = r'\(\d{3}\)\s\d{3}-\d{3}'
if re.fullmatch(pattern, phone):
    print(phone)
else:
    print('Invalid format')