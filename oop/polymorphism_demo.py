class Shape:
  def area (self):

    raise NotImplementedError(" ")
class Rectangle(Shape):
  def area(self, length, width):
    return length * width
  
class Circle (Shape):
  def area(self, radius):
    return math.pi * radius**2
  

    
