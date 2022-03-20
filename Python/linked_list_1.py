class Node:
    def __init__(self, data=None, nxt=None) -> None:
        self.data = data
        self.next = nxt
        # This is created because a node is like a box that contains data and position to the next data

class LinkedList:
    def __init__(self) -> None:
        # Head variable that points to the head of the list
        self.head = None 

    def insert_in_front(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_link(self):
        if not self.head: return print('My linked list is empty')
        else: 
            itr = self.head
            while itr:
                itr = itr.next

if __name__ == "__main__":
    pass