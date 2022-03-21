class HashTable:
    def __init__(self, limit=100):
        self.max = limit
        # self.array = [None for space in range(self.max)]
        # Introducing linked list to avoid collision
        self.array = [[] for space in range(self.max)]

    def get_hash(self, word):
        num = [ord(char) for char in word]  # Ord Function converts char to html symbol or entity
        return sum(num) % self.max  # A static function doesn't interact with class or instance variables

    def add(self, key, value):
        index = self.get_hash(key)
        # self.array[index] = value
        # We will set the item to overwrite if it already exists
        for idx, item in enumerate(self.array[index]):
            if len(item) == 2 and item[0] == key:
                self.array[index][idx] = (key, value)
                return 
            
        self.array[index].append((key, value))

    def get(self, key):
        index = self.get_hash(key)
        # return print(self.array[index])
        # Returns a list that we iterate and return the particular value
        for item in self.array[index]:
            if item[0] == key:
                return print(item[1])

    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, item in enumerate(self.array[index]):
            if item[0] == key:
                self.array[index].pop(idx)

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    


if __name__ == '__main__':
    hashT = HashTable()
    hashT.add('January 15th', 'I went to buy something')
    # hashT.get('January 15th')

    hashT.add('January 15th', 'I just bought from Jumia')
    hashT.add('February 13th', 'A day before the Valentine')
    # hashT.get('January 15th')

    hashT['February 14th'] = "I don't care about this day"
    # hashT['February 14th']
    
    del hashT['February 13th']
    hashT['February 13th']


