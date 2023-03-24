class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.memory = [None for item in range(self.size)]

    def get_hash(self, word):
        return sum([ord(item) for item in word]) % self.size

    def add(self, word, value):
        key = self.get_hash(word)
        self.memory[key] = value

    def get(self, word):
        key = self.get_hash(word)
        return self.memory[key]


ht = HashTable(10)
ht.add("name", "michael")
ht.get("nae")
ht.memory
