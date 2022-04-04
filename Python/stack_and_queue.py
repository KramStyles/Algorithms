from collections import deque

class Stack:
    def __init__(self) -> None:
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if not self.is_empty: return self.stack.pop()
        else: return print('Cannot remove from an empty Stack')


    def peek(self):
        return self.stack[-1]

    @property
    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

s = Stack()
s.push('Mental')
s.push('Dental')
s.pop()

def reverse_string(word):
    t = Stack()
    for char in word: t.push(char)
    ans = ''
    while t.stack:
        ans += t.pop()
    return ans

reverse_string('we will conquer')

class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self, val):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)