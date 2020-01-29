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
        #make current_node the given key
        current_node = self.storage.get(key)
        #if current_node is found move to front of the dic
        if current_node:
            self.cache.move_to_front(current_node)
            return current_node.value   
        #if not found then return None 
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
        #if key is already in dic we update value
        if key in self.storage.keys():
            updated_key = self.storage[key]
            updated_key.value = value
            self.cache.move_to_front(updated_key)
        #if there is room and no identical key we just add to dic
        else:
            self.cache.add_to_head(key, value)
            self.storage[key] = self.cache.head
        #if cache is at limit update tail to None
        if len(self.storage) > self.limit: 
            xpr_key = self.cache.tail.key
            self.storage[xpr_key] = None
            #remove tail node
            self.cache.remove_from_tail()
