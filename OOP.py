class Person:
    def __init__(self):
        self.age = 0
    def set_age(self,age):
        if age >= 0:
            self.age = age
        else:
            print('Ошибка! Возраст не должен быть отрицательным')
    def get_age(self):
        return self.age
P=Person()
print(P.set_age(27))
print(P.get_age())
P.set_age(-18)


class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "I'm an animal"
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "meow"
dog=Dog("Buddy")
cat=Cat("Kitty")
print(dog.name, dog.speak())
print(cat.name, cat.speak())



class Vehicle:
    def move(self):
        return "Vehicle is moving"
class Car(Vehicle):
    def move(self):
        return "Car is driving"
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"
car=Car()
bike=Bicycle()
print(car.move())
print(bike.move())



from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
rectangle=Rectangle(10,20)
circ=Circle(8)
print(rectangle.area())
print(circ.area())