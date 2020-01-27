import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #add to our queue size and add value to the head of the queue
        self.size += 1
        self.storage.add_to_head(value)
        
    def dequeue(self):
        #if we have no queue then return none
        if self.len() == 0:
            return None
        #if we have a queue then we will subtract from the size and remove the tail value
        else:
            self.size -= 1 
            return self.storage.remove_from_tail()

    def len(self):
        #return the size of our queue
        return self.size

