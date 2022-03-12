class Node:
    def __init__(self, val=None):
        self.value = val
        self.nextval = None


class SingleLinkedList:
    def __init__(self):
        self.headval = None

    def place_at_beginning(self, new_data):
        """
        implement the function to add a new node 
        at the beginning of the linked_list.
        """
        new_person = Node(new_data)
        new_person.nextval = self.headval
        self.headval = new_person
        

    def place_between(self, middle_node, new_data):
        """
        implement the function to add a new node 
        in the middle of the linked_list.
        """
        # 1. check if the given prev_node exists
        new_node = Node(new_data)
    
        
        new_node.next = prev_node.next
    
        # 5. make next of prev_node as new_node
        prev_node.next = new_node
        

    def place_at_end(self, new_data):
        """
        implement the function to add a new node 
        at the end of the linked_list
        """
        new_person = Node(new_data)
        if self.headval is None:
            self.headval = new_person

        last_person = self.headval
        while(last_person.nextval):
            last_person = last_person.nextval

        last_person.nextval = new_person

    def print_list(self):
        current_node = self.headval
        link = ""
        while current_node is not None:
            link += current_node.value
            current_node = current_node.nextval
            if current_node is not None:
                link += "-> "
        print(link)
