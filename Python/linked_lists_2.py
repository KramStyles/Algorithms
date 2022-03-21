class Node:
    def __init__(self, person=None, next_person=None):
        self.front_person = person
        self.next_person = next_person


class LinkedPersons:
    def __init__(self):
        self.front = None

    def place_person_in_front(self, person):
        new_person = Node(person, self.front)
        self.front = new_person

    def place_person_at_back(self, person):
        if not self.front:
            new_person = Node(person, self.front)
            self.front = new_person


if __name__ == '__main__':
    queue = LinkedPersons()
    queue.place_person_at_back('Ola')
    queue.place_person_in_front('Jeremiah')
    queue.place_person_in_front('Michelle')
