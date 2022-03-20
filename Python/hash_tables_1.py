class HashTable:
    def __init__(self):
        self.max = 100
        self.array = [None for space in range(self.max)]

    def get_hash(self, word):
        num = [ord(char) for char in word]  # Ord Function converts char to html symbol or entity
        return sum(num) % self.max  # A static function doesn't interact with class or instance variables
