# 1.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'


v1 = Vector(2, 3)
v2 = Vector(3, 4)

v3 = v1 + v2

print(v1)
print(v2)
print(v3)

# 2.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1 == book2)
print(book1 == book3)


# 3.


class Car:
    def __new__(cls, *args, **kwargs):
        print('Car object is being created')
        return super().__new__(cls)

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError('Brand must be string')
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str) or value == '':
            raise ValueError('Model must be a non-empty string')
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError('Year must be an integer')
        if value < 1886:
            raise ValueError('Invalid car year')
        self._year = value


car1 = Car('Toyota', 'Corolla', 2020)

print(car1.brand)
print(car1.model)
print(car1.year)

car1.year = 2022
print(car1.year)


car1.year = "2020"
