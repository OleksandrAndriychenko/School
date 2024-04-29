from time import *
class Auto():
    def __init__(self, brand, age, mark, cоlor = None, weight = 0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.cоlor = cоlor
        self.weight = weight

    def move(self):
        print('move')
    def birthday(self):
        age += 1
    def stop(self):
        print('stop')
class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, cоlor = None, weight = 0):
        super().__init__(brand, age, mark)
        self.cоlor = cоlor
        self.weight = weight
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()
    def load():
        sleep(1)
        print('load')
        sleep(1)
class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, cоlor = None, weight = 0):
        super().__init__(brand, age, mark)
        self.cоlor = cоlor
        self.weight = weight
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')
truck_1 = Truck('MAN', 12, 'R12', 25)
truck_2 = Truck('DAF',2, 'DF', 12)
car_1 = Car('BMW', 0, 'r32', 240)
car_2 = Car('Jeep', 3, 'cheroce', 180)
print(truck_1.__dict__)
print(truck_2.__dict__)
print(car_1.__dict__)
print(car_2.__dict__)


