class Stack(object):
    def __init__(self, length):
        self.stack = []
        self.length = length
    
    def push(self, value):
        if self.isFull():
            return 'Stack is full'
        self.stack.append(value)
    
    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        self.stack.pop()
        
    def isFull(self):
        return len(self.stack) == self.length
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def peek(self):
        return self.stack[-1]
    
    def __str__(self):
        return str(self.stack)
    
# Creatting stack
stack = Stack(2)
# Pushing to stack
stack.push(1)
print(stack)
stack.push(2)
print(stack)
stack.push(3)
print(stack)
# Pop the last item
stack.pop()
# push again
stack.push(4)
# Print the stack
print(stack)
# Get the peek element
print(stack.peek())
# Check is the stack is empty
print(stack.isEmpty())
