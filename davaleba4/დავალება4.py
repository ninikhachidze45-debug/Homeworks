# 1.
text = input('Enter text: ')
utf8 = text.encode("utf-8")
print(list(utf8))


# 2.
text = input('Enter text: ')
text = text.strip()
text = text.lower()
text += ' Python'
text = text.replace('python', 'Python')
print(text)


# 3.
text = input('Enter text: ')
half = len(text) // 2
print(text[:half])


# 4.
import string
text = input('Enter text: ')
letter = False
number = False
symbol = True

for char in text:
    if char in string.ascii_letters:
        letter = True
    elif char in string.digits:
        number = True
    else:
        symbol = False

if letter and number and symbol:
    print('Valid')
else:
    print('Invalid')


# 5.
text = input('Enter text: ')
bytes = text.encode('utf-8')
print(bytes)
text = bytes.decode('utf-8')
print(text)
