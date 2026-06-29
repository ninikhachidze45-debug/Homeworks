# 1.
sequence = input('Enter sequence: ').split()
set1 = set(sequence)
print(set1)


# 2.
sequence = input('Enter sequence: ').split()
frozenset1 = frozenset(sequence)
print(frozenset1)


# 3. 
set1 = {1, 3, 5, 7, 9}
set2 = {2, 4, 6, 8}
print(set1|set2)


# 4.
tuple1 = tuple(map(int, input('Enter numbers: ').split()))
print(list(tuple1))


# 5. 
list1 = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for i in list1:
    print(f'Name: {i[0]}, Age: {i[1]}')


# 6.
list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

print(set(list1) & set(list2))
