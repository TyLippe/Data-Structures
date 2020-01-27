import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        #add to our size and add the value given to the head of the stack
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        #check if we even have a stack to pop 
        if self.len() == 0:
            return None
        #if we have a stack, we will remove from the head and subtract one from out size
        else:
            self.size -= 1
            return self.storage.remove_from_head()
        
    def len(self):
        #return the size of our stack
        return self.size
