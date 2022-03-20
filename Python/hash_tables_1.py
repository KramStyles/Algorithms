class HashTable:
    def __init__(self, limit=100):
        self.max = limit
        self.array = [None for space in range(self.max)]

    def get_hash(self, word):
        num = [ord(char) for char in word]  # Ord Function converts char to html symbol or entity
        return sum(num) % self.max  # A static function doesn't interact with class or instance variables

    def add(self, key, value):
        index = self.get_hash(key)
        self.array[index] = value

    def get(self, key):
        index = self.get_hash(key)
        return print(self.array[index])

    def __setitem__(self, key, value):
        return self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)


if __name__ == '__main__':
    hashT = HashTable()
    hashT.add('January 15th', 'I went to buy something')
    hashT.get('January 15th')

    hashT['February 14th'] = "I don't care about this day"
    hashT['February 14th']
