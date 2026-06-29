# 1.

from pathlib import Path

def func(filename):
  with open(filename) as file_1:
    return Path(filename).resolve()
  
print(func('dicts.txt'))


# 2.

with open("dicts.txt") as file_1:
  content = file_1.read()
  print(content)



# 3.

file_1 = open('dicts.txt', 'a')
file_1.write("\n{'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56}")
file_1.write("\n{'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59}")
file_1.close()



# 4.

file_1 = open('dicts.txt', 'r+')
file_1.write('Hello world')
file_1.write('\nHello guys')
