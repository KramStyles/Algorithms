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
            return

        current_person = self.front
        while current_person.next_person:
            # print(current_person.next_person.front_person)
            current_person = current_person.next_person

        current_person.next_person = Node(person)

    def place_people_at_back(self, people: list):
        for person in people:
            self.place_person_at_back(person)

    def list_persons(self):
        persons = ''
        if not self.front:
            return print('No one is in the queue')
        else:
            current_person = self.front
            while current_person:
                persons += f" {current_person.front_person} --≥"
                current_person = current_person.next_person
        return print(persons[:-4])

    def reverse_people(self):
        persons = []
        while self.front:
            persons.append(self.front.front_person)
            self.front = self.front.next_person
        persons.reverse()
        self.place_people_at_back(persons)

    def number_of_people(self):
        people = 0
        while self.front:
            people += 1
            self.front = self.front.next_person
        return print('Number of people:', people)


if __name__ == '__main__':
    queue = LinkedPersons()
    queue.list_persons()
    queue.place_person_at_back('Ola')
    queue.place_person_in_front('Jeremiah')
    queue.place_person_in_front('Michelle')
    queue.place_person_at_back('Donald')
    queue.list_persons()
    queue.place_people_at_back(['Folu', 'Ebubue', 'Daniel', 'Okro'])
    queue.list_persons()
    queue.reverse_people()
    queue.list_persons()
    queue.number_of_people()
