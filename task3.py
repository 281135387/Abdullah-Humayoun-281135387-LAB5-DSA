from task1 import Stack
def reverse(s):
    stack = Stack()
    for i in s:
        stack.push(i)

    for j in range(stack.size()):
        reversest+= stack.pop()
    return reversest
