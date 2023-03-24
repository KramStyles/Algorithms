class Node:
    def __init__(self, value=None, next_value=None):
        self.lead_value = value
        self.next_value = next_value


class Atm:
    def __init__(self):
        self.head = None

    def put_person_in_front(self, data):
        person = Node(data, self.head)
        self.head = person

    def put_person_behind(self, data):
        people = self.head
        while people:
            print(people.lead_value)
            people = people.next_value

    def reverse(self):
        previous = None
        current = self.head
        next = self.head

        while current:
            next = next.next_value  # 2 8 4, 8 4,
            current.next_value = previous  # None, 12
            previous = current  # 12,
            current = next  # 2 8 4


atm = Atm()
atm.put_person_in_front(25)
atm.put_person_in_front(20)
atm.put_person_in_front(12)
atm.put_person_in_front(8)
atm.put_person_in_front(5)

atm.put_person_behind(1)

atm.reverse()
atm.put_person_behind(1)

print("hello")
