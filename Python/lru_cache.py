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
        self.recent = None

    def insertKeyValuePair(self, key, value):
        self.recent = key
        plain = {}
        for item in self.storage:
            plain[item[0]] = item[1]
        if key in plain:
            plain[key] = value
            self.storage = [(item, plain[item]) for item in plain]
            print(self.storage)
        elif len(self.storage) < self.maxSize:
            self.storage.append((key, value))
        else:
            del self.storage[0]
            self.storage.append((key, value))

    def getValueFromKey(self, key):
        plain = {}
        keys = []
        for item in self.storage:
            plain[item[0]] = item[1]
            keys.append(item[0])
        if key in plain:
            self.recent = key
            index = keys.index(key)
            self.sortQ(index)
            print(plain[key])
            return plain[key]
        return None

    def sortQ(self, index):
        for num in range(index, self.maxSize - 1):
            self.storage[num], self.storage[num + 1] = (
                self.storage[num + 1],
                self.storage[num],
            )

    def getMostRecentKey(self):
        print(self.storage[-1][0])
        return self.recent


q = LRUCache(4)
q.insertKeyValuePair("a", 1)
q.insertKeyValuePair("b", 2)
q.insertKeyValuePair("c", 3)
q.insertKeyValuePair("d", 4)
# q.getMostRecentKey() # c
q.getValueFromKey("a")  # 1
# q.getValueFromKey('b') # None
q.insertKeyValuePair("e", 5)

q.getValueFromKey("a")
