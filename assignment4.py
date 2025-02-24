'''Task 1: Create a Simple Calculator Class'''
class Calculator:
        
    def add(self, a, b):
        return a + b
    
    def substract(self, a , b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def devide(self, a, b):
        if b == 0:
            return "Cannot devide by zero"
        return a / b
    

calc = Calculator()

print("Addition: ",calc.add(5, 5))
print("Substraction: ", calc.substract(10, 5))
print("Multiplication: ", calc.multiply(5, 4))
print("Division: ", calc.devide(10, 5))



'''Task 2: Create a Circle Class'''
import math

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def areaOfCircle(self):
        return math.pi * (self.radius ** 2)
    
    def circumferenceofCircle(self):
        return 2 * math.pi * self.radius
    
circle = Circle(5)
print("Area of the Circle: ", round(circle.areaOfCircle(), 2))
print("Circumference of the Circle: ", round(circle.circumferenceofCircle(), 2))