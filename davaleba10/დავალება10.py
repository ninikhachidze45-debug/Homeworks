# 1.

def func(list1, list2):
    return list(zip(list1, list2))

numbers= [1, 2, 3]
letters = ['a', 'b', 'c']

print(func(numbers, letters))



# 2. 

from functools import reduce

def func(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError('Parameter must be a list')
        
        if not all(isinstance(i, (int, float)) for i in numbers):
            raise TypeError('ALL elements must be numbers')
        
        return reduce(lambda x, y: x * y, numbers)

    except TypeError as e:
        return e
    

print(func([1, 2, 3, 4, 5]))



# 3.

odd_numbers = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers([1, 2, 3, 4, 5, 6, 7]))



# 4. 

def func(strings, ending):
    if not isinstance(strings, list):
        raise TypeError('Parameter must be a list')
    
    if not isinstance(ending, str):
        raise TypeError('Second parameter must be a string')
    
    if not all(isinstance(s, str) for s in strings):
        raise TypeError('All elements in the list must be strings')
    
    return list(filter(lambda x: x.endswith(ending), strings))


print(func(['hello', 'world', 'coding', 'nod'], 'ing'))

    

