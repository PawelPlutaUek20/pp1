class Queue:

    def __init__(self):
        self.queue = []

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def enqueue(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue)==0
    
import random
q = Queue()
for i in range(5):
    q.enqueue(random.randint(-9,9))
for j in range(3):
    print(q.dequeue())