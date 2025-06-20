import math
class Shape:
  def area (self):

    raise NotImplementedError(" ")
class Rectangle(Shape):
  def __init__(self, length, width):
    super().__init__()
    self.length = length
    self.width = width
  def area(self, length, width):
    return length * width
  
class Circle(Shape):
  def __init__(self, radius):
    super().__init__()
    self.radius = radius
    
  def area(self, radius):
    return math.pi * radius ** 2