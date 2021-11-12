class Stack():
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        pop_value = None
        if self.isEmpty():
            print('stack is Empty')
        else:
            pop_value = self.stack.pop()
        return pop_value
    
    def top(self):
        top_value = None
        if self.isEmpty():
            print('Stack is Empty')
        else:
            top_value = self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0 :
            return True
        return False



# 스택 2개로 큐를 짜보세요.


stack1 = []
stack2 = []

