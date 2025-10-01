class Stack:
    def __init__(self):
        self.item = []

    def push(self,i):
        self.item.append(i)

    def is_empty(self):
        return len(self.item) == 0
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        return self.item.pop()
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        return self.item[-1]
    def size(self):
        return len(self.item)
    
s = Stack()
s.push(2)
s.push(3)

print(s.peek)
print(s.is_empty)
print(s.size)
