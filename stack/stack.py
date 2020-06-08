"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = [ ]

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append( value)

    def pop(self):
        return self.storage.pop()


test = Stack()
test.push('Eoin')
print(test.__len__())



class Node:
    def __init__(self, data=None):
        self.data = data

    def get_value(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_node):
        self.next_node = new_node