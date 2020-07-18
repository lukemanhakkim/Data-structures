"""
Author:Lukeman Hakkim
To implement the stack using Singly linkedlist
"""

class Node:

    def __init__(self):
        self.data = None
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data=data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next=next

    def has_next(self):
        return self.next!=None

class Stack(object):

    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp=Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head=temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.get_data()

my_list = ["luke", "hak", "arjun", "prawin"]
my_stack = Stack(my_list)
print(my_stack.pop())
print(my_stack.peek())






