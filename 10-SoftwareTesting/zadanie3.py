class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return (self.a*self.b)+(other.a*other.b)
    
p1 = Prostokat(3,2)
p2 = Prostokat(4,1)
print(p1+p2)