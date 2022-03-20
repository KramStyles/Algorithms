class Node:
    def __init__(self, data=None, nxt=None) -> None:
        self.data = data
        self.next = nxt
        # This is created because a node is like a box that contains data and position to the next data