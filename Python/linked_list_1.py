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

    def insert_at_end(self, data):
        new_data = Node(data)
        if not self.head:
            self.head = new_data
            return  

        itr = self.head
        while itr:
            itr = itr.next
        
        itr.next = new_data



    @property
    def print_link(self):
        if not self.head: return print('My linked list is empty')
        else: 
            itr = self.head
            arrow = ' --> '
            link = ''
            while itr:
                link += f'{itr.data}{arrow}'
                itr = itr.next
            print(link[:-5])

if __name__ == "__main__":
    link = LinkedList()
    link.insert_in_front(12)
    link.insert_in_front(69)
    link.insert_in_front(48)

    link.insert_at_end(5)


    link.print_link

    # NeetCode and Code basics
    # Blind 75 must do Leetcode