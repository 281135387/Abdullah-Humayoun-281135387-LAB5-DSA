from task1 import Stack

def parenthesischeck(exp):
    stack = Stack()
    pran={'(': ')','{':'}','[':']'}

    for i in exp:
        if i in '({[':
            stack.push(i)
        elif i in ')}]':
            stack.pop()
    return stack.is_empty()
