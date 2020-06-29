"""
Author: Lukeman Hakkim
Description: To implement stack operations using array
"""

class Stack(object):

    def __init__(self, limit=5):
        self.stk = []
        self.limit = limit

    def is_empty(self):
        return len(self.stk)<=0

    def push(self,item):
        if len(self.stk) >= self.limit:
            print("Stack Overflow")
        else:
            self.stk.append(item)
        print("stack after the push is : ",self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print("Warning !!!...... Stack Underflow")
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            print("Warning !!!...... Stack Underflow")
            return 0
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

my_stack = Stack(5)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.pop()
my_stack.pop()
print(my_stack.stk)
print(my_stack.peek())
print(my_stack.stk)




