from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #set limit to the given limit
        self.limit = limit
        #set cache to point to our DLL
        self.cache = DoublyLinkedList()
        #storage is a blank dic
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #if key is in the storage
        if key in self.storage.keys():
            #hold current node while we loop through the dic
            current_node = self.cache.head
            #loop 
            while current_node.key is not key:
                #check the next node for the key
                current_node = current_node.next    
            #when we find the correct key we will move it to the front
            self.cache.move_to_front(current_node)
            return current_node.value    
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #if cache is at limit 
        if len(self.storage) == self.limit: 
            #remove tail node
            self.cache.remove_from_tail()
            #add new key value to head
            self.cache.add_to_head(key, value)
            #add new key value to dic
            self.storage[key] = value
        #elif key is already in dic we update value
        elif key in self.storage.keys():
            self.storage[key] = value
            #start from head to look for our key value pair
            current_node = self.cache.head
            #loop through until we find the key in dic
            while current_node is not key:
                current_node = current_node.next
        #if there is room and no identical key we just add to dic
        else:
            self.cache.add_to_head(key, value)
            self.storage[key] = value
