class Queue:
    def __init__(self):
        self.item=[]
    def enqueue(self,i):
        self.item.append(i)
    def is_empty(self):
        return len(self.item) == 0
    def dequeue(self):
        if self.is_empty():
            print("stack is empty")
        return self.item.pop(0)
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        return self.item[0]
    def size(self):
        return len(self.item)
    
s = Queue()
s.enqueue(2)
s.enqueue(3)

print(s.dequeue)
print(s.is_empty)
print(s.size)
