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

    def reverse_people_without_list(self):
        # Todo: Runs into infinite loop.. Fix issue
        while self.front:
            self.place_person_at_back(self.front.front_person)
            self.front = self.front.next_person

    def number_of_people(self):
        people = 0
        current_people = self.front
        while current_people:
            people += 1
            current_people = current_people.next_person
        return people

    def remove_person_at(self, position: int):
        if position < 0 or position >= self.number_of_people():
            return print("Entry is invalid")
        elif position == 0:
            self.front = self.front.next_person
        else:
            counter = 0
            current_pos = self.front
            while current_pos:
                if counter == position - 1:
                    current_pos.next_person = current_pos.next_person.next_person
                    break
                current_pos = current_pos.next_person
                counter += 1


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
    print("Number of people in queue:", queue.number_of_people())

    queue.remove_person_at(0)  # Remove okro
    queue.remove_person_at(2)  # Remove folu
    queue.list_persons()
