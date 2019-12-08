import random
class Dice():
    def __init__(self):
        self.throw = random.randint(1,6)
    def result(self):
        print(self.throw)
        return self.throw
    
results = []
for _ in range(3):
    d = Dice()
    results.append(d.result())
print(sum(results))