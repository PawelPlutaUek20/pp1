class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0

import random
s = Stack()
for i in range(5):
    s.push(random.randint(-9,9))
for j in range(3):
    print(s.pop())