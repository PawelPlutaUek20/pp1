class Element: 
      
    def __init__(self, value): 
        self.value = value 
        self.next = None
        
    def __str__(self):
        return f'{self.value}'


class Queue: 
      
    def __init__(self): 
        self.front = None
        self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    def enqueue(self, element): 
        if self.rear == None: 
            self.front = self.rear = element
            return
        self.rear.next = element
        self.rear = element 
  
    def dequeue(self): 
        if self.isEmpty(): 
            return
        element = self.front 
        self.front = element.next
  
        if(self.front == None): 
            self.rear = None
        return str(element.value)
    
    def __str__(self):
        queue = ''
        element = self.front
        while element != None:
            queue += str(element)+'\n'
            element = element.next
        return queue
  

#utwórz kolejke
q = Queue()

# dodaj elementy do kolejki
print('Dodaję do kolejki')
element = Element(5)
print(element)
q.enqueue(element)

element = Element("abc")
print(element)
q.enqueue(element)

element = Element(True)
print(element)
q.enqueue(element)
  
# pokaż kolejke
print(f'\nZawartość kolejki\n{q}')

# zdejmij z kolejki
print('Zdejmuję z kolejki')
print(q.dequeue())

# pokaż kolejke
print(f'\nZawartość kolejki\n{q}')