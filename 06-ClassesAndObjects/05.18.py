class cube:
    import random
    def __init__(self):
        self.counter = 0
        
    def throw(self):
        return self.random.randint(1,6)
        
    def cubes(self, luck):
        x = luck
        y = luck
        return x,y
            
rc = cube()
luck = rc.throw()
print(rc.cubes(luck))
            