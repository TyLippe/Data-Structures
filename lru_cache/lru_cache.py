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
        #if does not exist we return none
        if key not in self.storage.keys():
            return None
        #find value that goes with the given key
        else:
            #move the key value pair to the end (tail)
            self.cache.move_to_end(key)
            #return the key's value
            return key.value

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
            #remove last entry
            self.cache.remove_from_tail()
        #overwrite key if it is already in the cache 
        elif key in self.storage.keys():
            self.storage.value = value
        #add key value pair to dict, making it most recent (add to end)