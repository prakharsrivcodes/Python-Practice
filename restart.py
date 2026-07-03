# import math as m
from math import pi
# print(pi)

# import sys
# print(sys.platform)
# print(sys.version)

# l = sys.argv
# print('hi', l[1], 'you are learning ', l[2])


class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("you drive the car")

    def stop(self):
        print("you stop the car")


car1 = Car("mustang", 2024, "red", False)
car2 = Car("Lamborghini", 8789, "green", True)

print(car1.model)
car1.drive()
car2.stop()

class Student:

    class_year = 2025
    def __init__(self,name,age):
        self.name = name
        self.age = age

student1 = Student("Praku", 20)
student2 = Student("oatrick", 35)
print(student1.class_year)
print(student1.name)


class Animal:
    def __init__(self, name, isAlive):
        self.name = name
        self.isAlive = True

    def eat(self):
        print("eat")
    
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog("scooby", True)
cat = Cat("tom", True)

print(dog.eat())


# super
class shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled
class Circle(shape):
   def __init__(self,color, filled, raidus):
        super().__init__(color, filled)
        self.raidus = raidus

class Square(shape):
       def __init__(self,color, filled, width):
        super().__init__(color,filled)
        self.width = width


class Triangle(shape):
       def __init__(self,color, filled, width, height):
        super().__init__(color,filled)
        self.width = width
        self.height = height

circle = Circle("blue",True,5)
print(circle.color)


# static methodt
# this is used when we want to create a method that is not dependent on the instance of the class. It can be called directly on the class itself without creating an object. toobejct abnao class me fir hceck kro not necessary u cna check it diretcly its simple
class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


print(Employee.is_valid_position("Manager"))          # True
print(Employee.is_valid_position("Rocket Scientist")) # False



# class method it is now used when we want to create a method that is dependent on the class itself rather than an instance of the class. It can be called directly on the class itself without creating an object. It takes the class as its first argument, which is conventionally named cls. This allows us to access and modify class-level attributes and methods.

class Student:

    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # Class Method
    @classmethod
    def get_count(cls):
        return f"Total Students: {cls.count}"

    # Static Method
    @staticmethod
    def is_valid_gpa(gpa):
        return 0 <= gpa <= 10


student1 = Student("Prakhar", 8.7)
student2 = Student("Aman", 9.2)

print(student1.get_info())          # Instance Method
print(Student.get_count())          # Class Method
print(Student.is_valid_gpa(8.5))    # Static Method
print(Student.is_valid_gpa(12))     # Static Method


# magic or dunder methods
# BELAAAR HAI

# PROPERTY GETTER SETTER
class Student:

    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value >= 0:
            self._marks = value
        else:
            print("Invalid Marks")


s = Student(90)

print(s.marks)   # Getter

s.marks = 95     # Setter

s.marks = -10    # Setter   
