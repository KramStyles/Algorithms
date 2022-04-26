# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods.
# Feel free to add new properties and methods to the class.
class LRUCache:
    """
        // All operations below are performed sequentially.
        LRUCache(3): - // instantiate an LRUCache of size 3
        insertKeyValuePair("b", 2): -
        insertKeyValuePair("a", 1): -
        insertKeyValuePair("c", 3): -
        getMostRecentKey(): "c" // "c" was the most recently inserted key
        getValueFromKey("a"): 1
        getMostRecentKey(): "a" // "a" was the most recently retrieved key
        insertKeyValuePair("d", 4): - // the cache had 3 entries; the least recently used one is evicted
        getValueFromKey("b"): None // "b" was evicted in the previous operation
        insertKeyValuePair("a", 5): - // "a" already exists in the cache so its value just gets replaced
        getValueFromKey("a"): 5
    """
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.storage = []

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        pass

    def getValueFromKey(self, key):
        # Write your code here.
        pass

    def getMostRecentKey(self):
        # Write your code here.
        pass