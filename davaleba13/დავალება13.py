
# 1.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')



car1 = Car('Toyota', 'Corolla', 2022)

car1.car_info()

# 2.


from datetime import datetime


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    
    def age_of_car(self):
        return datetime.now().year - self.year
    def car_info(self):
        print(f'Age of car: {self.age_of_car()}')

car1 = Car('Toyota', 'Corolla', 2022)

car1.car_info() 

# 3.

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f'ელემენტის ხანგრძლივობა შეადგენს {self.battery_life} საათს')


car1 = ElectricCar('Tesla', 'Model 3', 2023, 12)


car1.battery_info()




# 4, 5.

class Car:
    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1
       
    @classmethod
    def total_cars(cls):
        print(f'მანქანების საერთო რაოდენობაა: {cls.number_of_cars}')


car1 = Car('Toyota', 'Corolla', 2022)
car2 = Car('Tesla', 'Model 3', 2023)

Car.total_cars()