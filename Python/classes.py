class myset(set):
    def __init__(self, *values):
        self.values = set(values)

    def double_add(self, value):
        return self.values.add(value * 2)


numbs = myset(4, 5, 4, 3, 2, 8)
numbs.values.add(10)
numbs.double_add(15)
print((numbs.values))
