from typing import Any


class Animal:
    def __init__(self, name):
        self.name = name
        print("An animal has been born.")

    def eat(self):
        print("Munch Munch")

    def make_noise(self):
        print(f"Grrr says {self.name}")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A cat has been born.")

    def make_noise(self):
        print(f"Meow says {self.name}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("A dog has been born.")

    def make_noise(self):
        print(f"Bark says {self.name}")

def mainAnimals():
    cat = Cat("Kitty")
    dog1 = Dog("Doggy")
    dog2 = Dog("Doggo")
    animallist = [cat, dog1, dog2]
    for i in range(3):
        animallist[i].eat()
        animallist[i].make_noise()

mainAnimals()

class Cars:
    def __init__(self, make, model):
        self.__make = make
        self.__year_model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed
    
def mainCars():
    car = Cars("Toyota", 2022)
    for i in range(5): car.accelerate(); print(car.get_speed())
    for i in range(5): car.brake(); print(car.get_speed())

mainCars()

class Employees:
    def __init__(self, name, id, department, job):
        self.name = name
        self.id = id
        self.department = department
        self.job = job

def mainEmployees():
    emp1 = Employees("Susan Meyers", 47899, "Accounting", "Vice President")
    emp2 = Employees("Mark Jones", 39119, "IT", "Programmer")
    emp3 = Employees("Joy Rogers", 81774, "Manufacturing", "Engineer")
    print("Name ID Department Job")
    print(f"{emp1.name} {emp1.id} {emp1.department} {emp1.job}")
    print(f"{emp2.name} {emp2.id} {emp2.department} {emp2.job}")
    print(f"{emp3.name} {emp3.id} {emp3.department} {emp3.job}")

mainEmployees()