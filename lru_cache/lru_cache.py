class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = {}
        self.keys = []


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.pop(index)
            self.keys.append(key)
            return self.storage[key]
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
        entry = {key: value}
        # if the key is in list of keys
        if key in self.keys:
            # grabbing index of the key
            index = self.keys.index(key)
            # Popping key from list
            self.keys.pop(index)
            # Placing it back
            self.keys.append(key)
            # Deleting key, value from storage
            del self.storage[key]
            # adding key, value back to storage
            self.storage.update(entry)
        # Runs if key isn't in list of keys
        else:
            # Runs if size has reached limit
            if self.size == self.limit:
                # Grab first key in key list
                old_key = self.keys[0]
                # Delete it from storage
                del self.storage[old_key]
                # Delete it from List of keys
                self.keys.pop(0)
                # Add entry into storage
                self.storage.update(entry)
                # Add key into key list
                self.keys.append(key)
            # Runs if limit isn't reached
            else:
                # Updates storage with new entry
                self.storage.update(entry)
                # updates key list with new key
                self.keys.append(key)
                self.size += 1


                
                

