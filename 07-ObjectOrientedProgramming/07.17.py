import math
class Area():
    
    @staticmethod
    def area_circle(r):
        return math.pi*r**2
    @staticmethod
    def area_rectangle(a,b):
        return a*b
    @staticmethod
    def area_triangle(a,h):
        return a*h/2
    
print(Area.area_circle(3))
print(Area.area_rectangle(4,7))
print(Area.area_triangle(6,2)) 