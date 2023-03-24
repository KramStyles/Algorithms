from turtle import position


def searchinsortedmatrix(matrix, target):
    for idx, item in enumerate(matrix):
        for idx2, value in enumerate(item):
            if value == target:
                print(value, idx, idx2)
                return [idx, idx2]
    return [-1, -1]


# mat = [
#   [1, 4, 7, 12, 15, 1000],
#   [2, 5, 19, 31, 32, 1001],
#   [3, 8, 24, 33, 35, 1002],
#   [40, 41, 42, 44, 45, 1003],
#   [99, 100, 103, 106, 128, 1004],
# ]

# searchinsortedmatrix(mat, 45)


def longest_substring_without_duplication(string):
    holder = []
    general = []

    while string:
        for chars in string:
            if chars not in holder:
                holder.append(chars)
            else:
                break
        general.append("".join(holder))
        holder = []
        string = string[1:]

    print(max(general, key=len))
    return max(general, key=len)


# string1 = 'clementisacap'
# string2 = 'decadevsindecagonarelit'
# string3 = 'abcdeabcdefc'

# longest_substring_without_duplication(string1) # 'mentisac
# longest_substring_without_duplication(string2)
# longest_substring_without_duplication(string3)


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedPerson:
    def __init__(self) -> None:
        self.head = None

    def put_front(self, value):
        node = LinkedList(value)
        node.next = self.head
        self.head = node

    def total_number(self):
        total = 0
        current = self.head
        while current:
            total += 1
            current = current.next
        return total

    def remove_at(self, pos):
        if pos == 0:
            self.head = self.head.next
        else:
            counter = 0
            current_pos = self.head
            while current_pos:
                if counter == pos - 1:
                    current_pos.next = current_pos.next.next
                    break
                current_pos = current_pos.next
                counter += 1


def removeKthNodeFromEnd(node, k):

    pass


node = LinkedPerson()
node.put_front(9)
node.put_front(8)
node.put_front(7)
node.put_front(6)
node.put_front(5)
node.put_front(4)
node.put_front(3)
node.put_front(2)
node.put_front(1)
node.put_front(0)

print(node.total_number())
node.remove_at(5)
